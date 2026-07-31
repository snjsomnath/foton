use std::{
    sync::{
        Arc, Mutex,
        atomic::{AtomicBool, Ordering},
    },
    thread::{self, JoinHandle},
};

use serde::{Deserialize, Serialize};

use crate::{
    backend::{AnalysisRequest, AnalysisResult, Backend, SceneHandle},
    error::{DaylightError, Result},
};

#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum JobStatus {
    Queued,
    Running,
    Complete,
    Cancelled,
    Failed,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct JobSnapshot {
    pub status: JobStatus,
    pub progress: f32,
    pub solver_revision: u64,
    pub message: Option<String>,
}

pub struct AnalysisJob {
    cancelled: Arc<AtomicBool>,
    snapshot: Arc<Mutex<JobSnapshot>>,
    result: Arc<Mutex<Option<Result<AnalysisResult>>>>,
    thread: Option<JoinHandle<()>>,
}

impl AnalysisJob {
    pub fn spawn(backend: Arc<dyn Backend>, scene: SceneHandle, request: AnalysisRequest) -> Self {
        let solver_revision = scene.revision();
        let cancelled = Arc::new(AtomicBool::new(false));
        let snapshot = Arc::new(Mutex::new(JobSnapshot {
            status: JobStatus::Queued,
            progress: 0.0,
            solver_revision,
            message: None,
        }));
        let result = Arc::new(Mutex::new(None));

        let thread_cancelled = Arc::clone(&cancelled);
        let thread_snapshot = Arc::clone(&snapshot);
        let thread_result = Arc::clone(&result);
        let handle = thread::spawn(move || {
            {
                let mut current = thread_snapshot.lock().expect("job snapshot poisoned");
                current.status = JobStatus::Running;
            }
            let progress_snapshot = Arc::clone(&thread_snapshot);
            let progress = move |value: f32| {
                let mut current = progress_snapshot.lock().expect("job snapshot poisoned");
                current.progress = value.clamp(0.0, 1.0);
            };
            let analysis =
                backend.analyze_committed(&scene, &request, &thread_cancelled, &progress);
            let mut current = thread_snapshot.lock().expect("job snapshot poisoned");
            match &analysis {
                Ok(_) => {
                    current.status = JobStatus::Complete;
                    current.progress = 1.0;
                }
                Err(DaylightError::Cancelled) => {
                    current.status = JobStatus::Cancelled;
                    current.message = Some("analysis cancelled".into());
                }
                Err(error) => {
                    current.status = JobStatus::Failed;
                    current.message = Some(error.to_string());
                }
            }
            *thread_result.lock().expect("job result poisoned") = Some(analysis);
        });

        Self {
            cancelled,
            snapshot,
            result,
            thread: Some(handle),
        }
    }

    pub fn poll(&self) -> JobSnapshot {
        self.snapshot.lock().expect("job snapshot poisoned").clone()
    }

    pub fn cancel(&self) {
        self.cancelled.store(true, Ordering::Release);
    }

    pub fn cancellation_handle(&self) -> Arc<AtomicBool> {
        Arc::clone(&self.cancelled)
    }

    pub fn result(mut self) -> Result<AnalysisResult> {
        if let Some(handle) = self.thread.take() {
            handle.join().map_err(|_| DaylightError::Backend {
                detail: "analysis worker panicked".into(),
            })?;
        }
        self.result
            .lock()
            .expect("job result poisoned")
            .take()
            .unwrap_or_else(|| {
                Err(DaylightError::Backend {
                    detail: "analysis completed without a result".into(),
                })
            })
    }
}

impl Drop for AnalysisJob {
    fn drop(&mut self) {
        self.cancel();
        if let Some(handle) = self.thread.take() {
            let _ = handle.join();
        }
    }
}
