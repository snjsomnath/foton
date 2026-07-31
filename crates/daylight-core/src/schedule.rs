use serde::{Deserialize, Serialize};

use crate::error::{DaylightError, Result};

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OccupancySchedule {
    pub name: String,
    pub weights: Vec<f32>,
}

impl OccupancySchedule {
    pub fn new(name: impl Into<String>, weights: Vec<f32>) -> Result<Self> {
        let schedule = Self {
            name: name.into(),
            weights,
        };
        schedule.validate()?;
        Ok(schedule)
    }

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

    pub fn occupied_weight(&self) -> f32 {
        self.weights.iter().sum()
    }
}
