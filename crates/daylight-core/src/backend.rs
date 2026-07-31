use std::sync::{
    Arc, RwLock,
    atomic::{AtomicBool, AtomicU64, Ordering},
};

use serde::{Deserialize, Serialize};

use crate::{
    error::{DaylightError, Result},
    geometry::SceneData,
    metrics::{AnnualMetrics, DaylightFactorMetrics},
    sky::{CoefficientMatrix, SkyBasis, SkyMatrix},
};

#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum AnalysisQuality {
    Preview,
    Final,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct AnalysisRequest {
    pub sky: SkyMatrix,
    pub occupancy_weights: Vec<f32>,
    pub quality: AnalysisQuality,
    pub threshold_lux: f32,
    pub time_fraction: f32,
    pub maximum_samples: u32,
    pub maximum_bounces: u32,
    pub scene_seed: u64,
    pub export_coefficients: bool,
}

#[derive(Clone, Debug, Default, PartialEq, Serialize, Deserialize)]
pub struct GpuTimings {
    pub upload_ms: f64,
    pub acceleration_structure_ms: f64,
    pub tracing_ms: f64,
    pub annual_reduction_ms: f64,
    pub snapshot_ms: f64,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct AnalysisResult {
    pub solver_revision: u64,
    pub coefficients: Option<CoefficientMatrix>,
    pub annual: AnnualMetrics,
    pub daylight_factor: Option<DaylightFactorMetrics>,
    pub sample_count: u32,
    pub bounce_count: u32,
    pub timings: GpuTimings,
    pub metadata: AnalysisMetadata,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct AnalysisMetadata {
    pub metric_label: String,
    pub solver_version: String,
    pub scene_fingerprint: u64,
    pub basis: SkyBasis,
    pub quality: AnalysisQuality,
    pub glazing_model: String,
    pub schedule_timestep_count: usize,
    pub convergence: f32,
    pub transport_backend: String,
    pub used_reference_fallback: bool,
}

#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub struct BackendCapabilities {
    pub name: String,
    pub hardware_acceleration: bool,
    pub supports_ray_tracing: bool,
    pub supports_async_jobs: bool,
}

static NEXT_SCENE_ID: AtomicU64 = AtomicU64::new(1);

#[derive(Clone)]
pub struct SceneHandle {
    id: u64,
    revision: Arc<AtomicU64>,
    data: Arc<RwLock<SceneData>>,
}

impl SceneHandle {
    pub fn new(mut scene: SceneData) -> Result<Self> {
        scene.validate()?;
        Ok(Self {
            id: NEXT_SCENE_ID.fetch_add(1, Ordering::Relaxed),
            revision: Arc::new(AtomicU64::new(1)),
            data: Arc::new(RwLock::new(scene)),
        })
    }

    pub const fn id(&self) -> u64 {
        self.id
    }

    pub fn revision(&self) -> u64 {
        self.revision.load(Ordering::Acquire)
    }

    pub fn snapshot(&self) -> Result<SceneData> {
        self.data
            .read()
            .map(|scene| scene.clone())
            .map_err(|_| DaylightError::Backend {
                detail: "scene handle lock is poisoned".into(),
            })
    }

    pub fn update_instances(&self, updates: &[InstanceUpdate]) -> Result<u64> {
        let mut scene = self.data.write().map_err(|_| DaylightError::Backend {
            detail: "scene handle lock is poisoned".into(),
        })?;
        let mut updated_scene = scene.clone();
        for update in updates {
            let instance = updated_scene
                .instances
                .get_mut(update.instance_index)
                .ok_or_else(|| DaylightError::InvalidValue {
                    field: "instance_updates.instance_index",
                    detail: format!("instance {} is out of range", update.instance_index),
                })?;
            instance.transform = update.transform;
            if let Some(room_id) = update.room_id {
                instance.room_id = room_id;
            }
        }
        updated_scene.validate()?;
        *scene = updated_scene;
        Ok(self.revision.fetch_add(1, Ordering::AcqRel) + 1)
    }
}

#[derive(Clone, Copy, Debug)]
pub struct InstanceUpdate {
    pub instance_index: usize,
    pub transform: [f32; 16],
    pub room_id: Option<u32>,
}

pub trait Backend: Send + Sync + 'static {
    fn capabilities(&self) -> BackendCapabilities;

    fn commit_scene(&self, scene: SceneData) -> Result<SceneHandle> {
        SceneHandle::new(scene)
    }

    fn update_instances(&self, handle: &SceneHandle, updates: &[InstanceUpdate]) -> Result<u64> {
        handle.update_instances(updates)
    }

    fn analyze_committed(
        &self,
        handle: &SceneHandle,
        request: &AnalysisRequest,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
    ) -> Result<AnalysisResult> {
        self.analyze(
            &handle.snapshot()?,
            request,
            handle.revision(),
            cancelled,
            progress,
        )
    }

    fn analyze(
        &self,
        scene: &SceneData,
        request: &AnalysisRequest,
        solver_revision: u64,
        cancelled: &AtomicBool,
        progress: &(dyn Fn(f32) + Send + Sync),
    ) -> Result<AnalysisResult>;
}
