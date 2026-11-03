pub mod backend;
pub mod error;
pub mod fixtures;
pub mod geometry;
pub mod hash;
pub mod job;
pub mod material;
pub mod metrics;
pub mod sampling;
pub mod schedule;
pub mod sky;

pub use backend::{
    AnalysisMetadata, AnalysisQuality, AnalysisRequest, AnalysisResult, AnnualIlluminance, Backend,
    BackendCapabilities, GpuTimings, InstanceUpdate, SceneHandle,
};
pub use error::{DaylightError, Result};
pub use fixtures::{
    MASK_ACTIVE_BATCH, MASK_EXTERIOR, MASK_GLAZING, MASK_OPAQUE, ShoeboxOptions, shoebox_scene,
};
pub use geometry::{Instance, Material, MaterialKind, MeshRange, SceneData, Sensor, Vec3};
pub use hash::scene_fingerprint;
pub use job::{AnalysisJob, JobSnapshot, JobStatus};
pub use material::{
    fresnel_reflectance, radiance_glass_transmissivity, thin_glass_reflectance_from_transmissivity,
    thin_glass_transmittance, thin_glass_transmittance_from_transmissivity,
};
pub use metrics::{
    AnnualMetrics, DaylightFactorMetrics, SensorAnnualMetric, annual_metrics_from_accumulators,
    annual_metrics_from_weights, evaluate_daylight_factor, reduce_annual_metrics,
};
pub use sampling::{SampleKey, cosine_hemisphere, low_discrepancy_sample, sobol_uint};
pub use schedule::OccupancySchedule;
pub use sky::{
    CoefficientMatrix, REINHART_MF2_ROWS, SkyBasis, SkyMatrix, TREGENZA_ROWS, closest_patch,
    mf2_to_tregenza_map, patch_directions, patch_sample_directions, patch_solid_angles,
    radiance_patch_index,
};

pub const SOLVER_VERSION: &str = env!("CARGO_PKG_VERSION");
