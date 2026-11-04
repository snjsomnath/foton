use serde::{Deserialize, Serialize};

use crate::error::{DaylightError, Result};

/// An occupancy schedule: one weight from 0 to 1 per timestep.
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OccupancySchedule {
    pub name: String,
    pub weights: Vec<f32>,
}

impl OccupancySchedule {
    /// Create a schedule and check it.
    pub fn new(name: impl Into<String>, weights: Vec<f32>) -> Result<Self> {
        let schedule = Self {
            name: name.into(),
            weights,
        };
        schedule.validate()?;
        Ok(schedule)
    }

    /// Check that the schedule has a name, valid weights and some occupied time.
    pub fn validate(&self) -> Result<()> {
        if self.name.trim().is_empty() || self.weights.is_empty() {
            return Err(DaylightError::InvalidShape {
                field: "occupancy_schedule",
                detail: "name and weights must be non-empty".into(),
            });
        }
        if self
            .weights
            .iter()
            .any(|weight| !weight.is_finite() || *weight < 0.0 || *weight > 1.0)
        {
            return Err(DaylightError::InvalidValue {
                field: "occupancy_schedule.weights",
                detail: "weights must be finite and within [0, 1]".into(),
            });
        }
        if self.occupied_weight() <= 0.0 {
            return Err(DaylightError::InvalidValue {
                field: "occupancy_schedule.weights",
                detail: "schedule must contain occupied time".into(),
            });
        }
        Ok(())
    }

    /// Total occupied time, the sum of the weights.
    pub fn occupied_weight(&self) -> f32 {
        self.weights.iter().sum()
    }
}
