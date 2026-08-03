use std::collections::BTreeMap;

use serde::{Deserialize, Serialize};

use crate::{
    error::{DaylightError, Result},
    geometry::Sensor,
    sky::{CoefficientMatrix, SkyMatrix},
};

const PHOTOPIC_WEIGHTS: [f32; 3] = [47.435, 119.93, 11.635];

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct SensorAnnualMetric {
    pub sensor_id: u32,
    pub room_id: u32,
    pub daylight_autonomy: f32,
    pub continuous_daylight_autonomy: f32,
    pub useful_daylight_illuminance_lower: f32,
    pub useful_daylight_illuminance: f32,
    pub useful_daylight_illuminance_upper: f32,
    pub passes_sda: bool,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct RoomAnnualMetric {
    pub room_id: u32,
    pub static_sda_300_50: f32,
    pub represented_area: f32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct AnnualMetrics {
    pub threshold_lux: f32,
    pub udi_lower_lux: f32,
    pub udi_upper_lux: f32,
    pub time_fraction: f32,
    pub occupied_weight: f32,
    pub sensors: Vec<SensorAnnualMetric>,
    pub rooms: Vec<RoomAnnualMetric>,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct DaylightFactorMetrics {
    pub per_sensor_percent: Vec<f32>,
    pub mean_percent: f32,
    pub minimum_percent: f32,
    pub maximum_percent: f32,
}

pub fn reduce_annual_metrics(
    coefficients: &CoefficientMatrix,
    sky: &SkyMatrix,
    occupancy_weights: &[f32],
    sensors: &[Sensor],
    threshold_lux: f32,
    udi_lower_lux: f32,
    udi_upper_lux: f32,
    time_fraction: f32,
) -> Result<AnnualMetrics> {
    coefficients.validate()?;
    sky.validate()?;
    if coefficients.basis != sky.basis {
        return Err(DaylightError::InvalidValue {
            field: "sky.basis",
            detail: "coefficient and sky bases must match".into(),
        });
    }
    if coefficients.sensor_count != sensors.len() {
        return Err(DaylightError::InvalidShape {
            field: "sensors",
            detail: "sensor count must match coefficient rows".into(),
        });
    }
    if occupancy_weights.len() != sky.timestep_count {
        return Err(DaylightError::InvalidShape {
            field: "occupancy_weights",
            detail: "schedule length must match sky timesteps".into(),
        });
    }
    if !threshold_lux.is_finite()
        || threshold_lux <= 0.0
        || !udi_lower_lux.is_finite()
        || udi_lower_lux < 0.0
        || !udi_upper_lux.is_finite()
        || udi_upper_lux <= udi_lower_lux
        || !time_fraction.is_finite()
        || !(0.0..=1.0).contains(&time_fraction)
        || occupancy_weights
            .iter()
            .any(|weight| !weight.is_finite() || *weight < 0.0)
    {
        return Err(DaylightError::InvalidValue {
            field: "annual metrics",
            detail: "threshold, time fraction, and occupancy weights are invalid".into(),
        });
    }
    let occupied_weight: f32 = occupancy_weights.iter().sum();
    if occupied_weight <= 0.0 {
        return Err(DaylightError::InvalidValue {
            field: "occupancy_weights",
            detail: "schedule must contain occupied time".into(),
        });
    }

    let patch_count = coefficients.basis.row_count();
    let mut above_threshold_weights = Vec::with_capacity(sensors.len());
    let mut continuous_weights = Vec::with_capacity(sensors.len());
    let mut udi_lower_weights = Vec::with_capacity(sensors.len());
    let mut udi_weights = Vec::with_capacity(sensors.len());
    let mut udi_upper_weights = Vec::with_capacity(sensors.len());
    for sensor_index in 0..sensors.len() {
        let mut above_threshold_weight = 0.0;
        let mut continuous_weight = 0.0;
        let mut udi_lower_weight = 0.0;
        let mut udi_weight = 0.0;
        let mut udi_upper_weight = 0.0;
        for (timestep_index, occupancy_weight) in occupancy_weights.iter().copied().enumerate() {
            if occupancy_weight == 0.0 {
                continue;
            }
            let mut response_rgb = [0.0_f32; 3];
            for patch_index in 0..patch_count {
                let coefficient = coefficients.get(sensor_index, patch_index);
                let sky_value = sky.get(patch_index, timestep_index);
                for component in 0..3 {
                    response_rgb[component] += coefficient[component] * sky_value[component];
                }
            }
            let illuminance = response_rgb
                .iter()
                .zip(PHOTOPIC_WEIGHTS)
                .map(|(value, weight)| value * weight)
                .sum::<f32>();
            if illuminance >= threshold_lux {
                above_threshold_weight += occupancy_weight;
            }
            continuous_weight += occupancy_weight * (illuminance / threshold_lux).clamp(0.0, 1.0);
            if illuminance < udi_lower_lux {
                udi_lower_weight += occupancy_weight;
            } else if illuminance <= udi_upper_lux {
                udi_weight += occupancy_weight;
            } else {
                udi_upper_weight += occupancy_weight;
            }
        }
        above_threshold_weights.push(above_threshold_weight);
        continuous_weights.push(continuous_weight);
        udi_lower_weights.push(udi_lower_weight);
        udi_weights.push(udi_weight);
        udi_upper_weights.push(udi_upper_weight);
    }
    annual_metrics_from_accumulators(
        sensors,
        occupied_weight,
        &above_threshold_weights,
        &continuous_weights,
        &udi_lower_weights,
        &udi_weights,
        &udi_upper_weights,
        threshold_lux,
        udi_lower_lux,
        udi_upper_lux,
        time_fraction,
    )
}

pub fn annual_metrics_from_weights(
    sensors: &[Sensor],
    occupied_weight: f32,
    above_threshold_weights: &[f32],
    threshold_lux: f32,
    time_fraction: f32,
) -> Result<AnnualMetrics> {
    let zeros = vec![0.0; sensors.len()];
    annual_metrics_from_accumulators(
        sensors,
        occupied_weight,
        above_threshold_weights,
        &zeros,
        &zeros,
        &zeros,
        &zeros,
        threshold_lux,
        100.0,
        3000.0,
        time_fraction,
    )
}

#[allow(clippy::too_many_arguments)]
pub fn annual_metrics_from_accumulators(
    sensors: &[Sensor],
    occupied_weight: f32,
    above_threshold_weights: &[f32],
    continuous_weights: &[f32],
    udi_lower_weights: &[f32],
    udi_weights: &[f32],
    udi_upper_weights: &[f32],
    threshold_lux: f32,
    udi_lower_lux: f32,
    udi_upper_lux: f32,
    time_fraction: f32,
) -> Result<AnnualMetrics> {
    let accumulator_lengths = [
        above_threshold_weights.len(),
        continuous_weights.len(),
        udi_lower_weights.len(),
        udi_weights.len(),
        udi_upper_weights.len(),
    ];
    if sensors.is_empty()
        || accumulator_lengths
            .iter()
            .any(|length| *length != sensors.len())
    {
        return Err(DaylightError::InvalidShape {
            field: "annual_metric_accumulators",
            detail: "every accumulator must contain one value per sensor".into(),
        });
    }
    if !occupied_weight.is_finite()
        || occupied_weight <= 0.0
        || [
            above_threshold_weights,
            continuous_weights,
            udi_lower_weights,
            udi_weights,
            udi_upper_weights,
        ]
        .into_iter()
        .flatten()
        .any(|weight| !weight.is_finite() || *weight < 0.0 || *weight > occupied_weight)
        || !threshold_lux.is_finite()
        || threshold_lux <= 0.0
        || !udi_lower_lux.is_finite()
        || udi_lower_lux < 0.0
        || !udi_upper_lux.is_finite()
        || udi_upper_lux <= udi_lower_lux
        || !time_fraction.is_finite()
        || !(0.0..=1.0).contains(&time_fraction)
    {
        return Err(DaylightError::InvalidValue {
            field: "annual weights",
            detail: "occupied and above-threshold weights are invalid".into(),
        });
    }

    let mut sensor_metrics = Vec::with_capacity(sensors.len());
    let mut room_areas: BTreeMap<u32, (f32, f32)> = BTreeMap::new();
    for (index, sensor) in sensors.iter().enumerate() {
        let above_threshold_weight = above_threshold_weights[index];
        let daylight_autonomy = above_threshold_weight / occupied_weight;
        let passes_sda = daylight_autonomy >= time_fraction;
        sensor_metrics.push(SensorAnnualMetric {
            sensor_id: sensor.sensor_id,
            room_id: sensor.room_id,
            daylight_autonomy,
            continuous_daylight_autonomy: continuous_weights[index] / occupied_weight,
            useful_daylight_illuminance_lower: udi_lower_weights[index] / occupied_weight,
            useful_daylight_illuminance: udi_weights[index] / occupied_weight,
            useful_daylight_illuminance_upper: udi_upper_weights[index] / occupied_weight,
            passes_sda,
        });
        let room_area = room_areas.entry(sensor.room_id).or_default();
        room_area.0 += sensor.area_weight;
        if passes_sda {
            room_area.1 += sensor.area_weight;
        }
    }
    let rooms = room_areas
        .into_iter()
        .map(
            |(room_id, (represented_area, passing_area))| RoomAnnualMetric {
                room_id,
                static_sda_300_50: 100.0 * passing_area / represented_area,
                represented_area,
            },
        )
        .collect();
    Ok(AnnualMetrics {
        threshold_lux,
        udi_lower_lux,
        udi_upper_lux,
        time_fraction,
        occupied_weight,
        sensors: sensor_metrics,
        rooms,
    })
}

pub fn evaluate_daylight_factor(
    interior_illuminance: &[f32],
    exterior_horizontal_illuminance: f32,
) -> Result<DaylightFactorMetrics> {
    if interior_illuminance.is_empty()
        || !exterior_horizontal_illuminance.is_finite()
        || exterior_horizontal_illuminance <= 0.0
        || interior_illuminance
            .iter()
            .any(|value| !value.is_finite() || *value < 0.0)
    {
        return Err(DaylightError::InvalidValue {
            field: "daylight factor",
            detail: "interior values must be non-negative and exterior illuminance positive".into(),
        });
    }
    let per_sensor_percent = interior_illuminance
        .iter()
        .map(|value| 100.0 * value / exterior_horizontal_illuminance)
        .collect::<Vec<_>>();
    let mean_percent = per_sensor_percent.iter().sum::<f32>() / per_sensor_percent.len() as f32;
    let minimum_percent = per_sensor_percent
        .iter()
        .copied()
        .fold(f32::INFINITY, f32::min);
    let maximum_percent = per_sensor_percent
        .iter()
        .copied()
        .fold(f32::NEG_INFINITY, f32::max);
    Ok(DaylightFactorMetrics {
        per_sensor_percent,
        mean_percent,
        minimum_percent,
        maximum_percent,
    })
}
