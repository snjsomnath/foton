use serde::{Deserialize, Serialize};

use crate::{
    error::{DaylightError, Result},
    geometry::Vec3,
};

pub const TREGENZA_ROWS: usize = 146;
pub const REINHART_MF2_ROWS: usize = 578;
const TREGENZA_RING_COUNTS: [usize; 7] = [30, 30, 24, 24, 18, 12, 6];
const TREGENZA_RING_ALTITUDES_DEGREES: [f32; 7] = [6.0, 18.0, 30.0, 42.0, 54.0, 66.0, 78.0];

#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum SkyBasis {
    Tregenza,
    ReinhartMf2,
}

impl SkyBasis {
    pub const fn row_count(self) -> usize {
        match self {
            Self::Tregenza => TREGENZA_ROWS,
            Self::ReinhartMf2 => REINHART_MF2_ROWS,
        }
    }
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct CoefficientMatrix {
    pub sensor_count: usize,
    pub basis: SkyBasis,
    pub values: Vec<[f32; 3]>,
}

impl CoefficientMatrix {
    pub fn new(sensor_count: usize, basis: SkyBasis, values: Vec<[f32; 3]>) -> Result<Self> {
        let matrix = Self {
            sensor_count,
            basis,
            values,
        };
        matrix.validate()?;
        Ok(matrix)
    }

    pub fn validate(&self) -> Result<()> {
        let expected = self.sensor_count * self.basis.row_count();
        if self.sensor_count == 0 || self.values.len() != expected {
            return Err(DaylightError::InvalidShape {
                field: "coefficients",
                detail: format!("expected {expected} RGB values, got {}", self.values.len()),
            });
        }
        if self
            .values
            .iter()
            .flatten()
            .any(|value| !value.is_finite() || *value < 0.0)
        {
            return Err(DaylightError::InvalidValue {
                field: "coefficients",
                detail: "values must be finite and non-negative".into(),
            });
        }
        Ok(())
    }

    pub fn get(&self, sensor_index: usize, patch_index: usize) -> [f32; 3] {
        self.values[sensor_index * self.basis.row_count() + patch_index]
    }

    pub fn aggregate_tregenza(&self) -> Result<Self> {
        if self.basis == SkyBasis::Tregenza {
            return Ok(self.clone());
        }
        let mapping = mf2_to_tregenza_map();
        let mut values = vec![[0.0; 3]; self.sensor_count * TREGENZA_ROWS];
        for sensor_index in 0..self.sensor_count {
            for (mf2_patch, tregenza_patch) in mapping.iter().copied().enumerate() {
                let source = self.get(sensor_index, mf2_patch);
                let destination = &mut values[sensor_index * TREGENZA_ROWS + tregenza_patch];
                for component in 0..3 {
                    destination[component] += source[component];
                }
            }
        }
        Self::new(self.sensor_count, SkyBasis::Tregenza, values)
    }
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct SkyMatrix {
    pub basis: SkyBasis,
    pub timestep_count: usize,
    pub values: Vec<[f32; 3]>,
}

impl SkyMatrix {
    pub fn new(basis: SkyBasis, timestep_count: usize, values: Vec<[f32; 3]>) -> Result<Self> {
        let matrix = Self {
            basis,
            timestep_count,
            values,
        };
        matrix.validate()?;
        Ok(matrix)
    }

    pub fn validate(&self) -> Result<()> {
        let expected = self.basis.row_count() * self.timestep_count;
        if self.timestep_count == 0 || self.values.len() != expected {
            return Err(DaylightError::InvalidShape {
                field: "sky",
                detail: format!("expected {expected} RGB values, got {}", self.values.len()),
            });
        }
        if self
            .values
            .iter()
            .flatten()
            .any(|value| !value.is_finite() || *value < 0.0)
        {
            return Err(DaylightError::InvalidValue {
                field: "sky",
                detail: "values must be finite and non-negative".into(),
            });
        }
        Ok(())
    }

    pub fn get(&self, patch_index: usize, timestep_index: usize) -> [f32; 3] {
        self.values[patch_index * self.timestep_count + timestep_index]
    }
}

pub fn mf2_to_tregenza_map() -> Vec<usize> {
    let mut mapping = vec![0; REINHART_MF2_ROWS];
    let mut mf2_offset = 1;
    let mut tregenza_offset = 1;
    for parent_count in TREGENZA_RING_COUNTS {
        for _altitude_child in 0..2 {
            for azimuth_child in 0..(parent_count * 2) {
                mapping[mf2_offset + azimuth_child] = tregenza_offset + azimuth_child / 2;
            }
            mf2_offset += parent_count * 2;
        }
        tregenza_offset += parent_count;
    }
    mapping[REINHART_MF2_ROWS - 1] = TREGENZA_ROWS - 1;
    mapping
}

pub fn patch_directions(basis: SkyBasis) -> Vec<Vec3> {
    let mut directions = Vec::with_capacity(basis.row_count());
    directions.push(Vec3::new(0.0, 0.0, -1.0));
    match basis {
        SkyBasis::Tregenza => {
            for (ring_index, patch_count) in TREGENZA_RING_COUNTS.iter().copied().enumerate() {
                append_ring(
                    &mut directions,
                    TREGENZA_RING_ALTITUDES_DEGREES[ring_index],
                    patch_count,
                    0.0,
                );
            }
        }
        SkyBasis::ReinhartMf2 => {
            let multiplier = 2;
            let altitude_increment = 90.0 / (multiplier as f32 * 7.0 + 0.5);
            for subring in 0..(TREGENZA_RING_COUNTS.len() * multiplier) {
                let parent_ring = (subring as f32 + 0.5).floor() as usize / multiplier;
                append_ring(
                    &mut directions,
                    (subring as f32 + 0.5) * altitude_increment,
                    TREGENZA_RING_COUNTS[parent_ring] * multiplier,
                    0.0,
                );
            }
        }
    }
    directions.push(Vec3::new(0.0, 0.0, 1.0));
    directions
}

pub fn patch_solid_angles(basis: SkyBasis) -> Vec<f32> {
    let mut solid_angles = Vec::with_capacity(basis.row_count());
    solid_angles.push(std::f32::consts::TAU);
    match basis {
        SkyBasis::Tregenza => {
            for (ring_index, patch_count) in TREGENZA_RING_COUNTS.iter().copied().enumerate() {
                let lower = (ring_index as f32 * 12.0).to_radians();
                let upper = ((ring_index + 1) as f32 * 12.0).to_radians();
                let ring_solid_angle = std::f32::consts::TAU * (upper.sin() - lower.sin());
                solid_angles.extend(std::iter::repeat_n(
                    ring_solid_angle / patch_count as f32,
                    patch_count,
                ));
            }
        }
        SkyBasis::ReinhartMf2 => {
            let multiplier = 2;
            let altitude_increment = 90.0 / (multiplier as f32 * 7.0 + 0.5);
            for subring in 0..(TREGENZA_RING_COUNTS.len() * multiplier) {
                let parent_ring = (subring as f32 + 0.5).floor() as usize / multiplier;
                let lower = (subring as f32 * altitude_increment).to_radians();
                let upper = ((subring + 1) as f32 * altitude_increment).to_radians();
                let patch_count = TREGENZA_RING_COUNTS[parent_ring] * multiplier;
                let ring_solid_angle = std::f32::consts::TAU * (upper.sin() - lower.sin());
                solid_angles.extend(std::iter::repeat_n(
                    ring_solid_angle / patch_count as f32,
                    patch_count,
                ));
            }
        }
    }
    let cap_lower = match basis {
        SkyBasis::Tregenza => 84.0_f32,
        SkyBasis::ReinhartMf2 => 14.0_f32 * (90.0_f32 / 14.5_f32),
    }
    .to_radians();
    solid_angles.push(std::f32::consts::TAU * (1.0 - cap_lower.sin()));
    solid_angles
}

pub fn closest_patch(basis: SkyBasis, direction: Vec3) -> usize {
    if direction.z < 0.0 {
        return 0;
    }
    patch_directions(basis)
        .iter()
        .enumerate()
        .skip(1)
        .max_by(|(_, left), (_, right)| left.dot(direction).total_cmp(&right.dot(direction)))
        .map(|(index, _)| index)
        .unwrap_or(basis.row_count() - 1)
}

pub fn radiance_patch_index(basis: SkyBasis, direction: Vec3) -> usize {
    if direction.z < 0.0 {
        return 0;
    }
    let multiplier = match basis {
        SkyBasis::Tregenza => 1,
        SkyBasis::ReinhartMf2 => 2,
    };
    let regular_row_count = TREGENZA_RING_COUNTS.len() * multiplier;
    let altitude_increment = 90.0_f32.to_radians() / (regular_row_count as f32 + 0.5);
    let row = (direction.z.clamp(-1.0, 1.0).asin() / altitude_increment).floor() as usize;
    if row >= regular_row_count {
        return basis.row_count() - 1;
    }

    let patch_count = TREGENZA_RING_COUNTS
        [((row as f32 + 0.5) / multiplier as f32).floor() as usize]
        * multiplier;
    let offset = 1
        + (0..row)
            .map(|prior_row| {
                TREGENZA_RING_COUNTS
                    [((prior_row as f32 + 0.5) / multiplier as f32).floor() as usize]
                    * multiplier
            })
            .sum::<usize>();
    let mut azimuth = direction.x.atan2(direction.y);
    if azimuth < 0.0 {
        azimuth += std::f32::consts::TAU;
    }
    let azimuth_increment = std::f32::consts::TAU / patch_count as f32;
    let azimuth_index =
        ((azimuth + 0.5 * azimuth_increment) / azimuth_increment).floor() as usize % patch_count;
    offset + azimuth_index
}

fn append_ring(
    directions: &mut Vec<Vec3>,
    altitude_degrees: f32,
    patch_count: usize,
    azimuth_offset: f32,
) {
    let altitude = altitude_degrees.to_radians();
    let horizontal = altitude.cos();
    for patch_index in 0..patch_count {
        let azimuth =
            (patch_index as f32 + azimuth_offset) * std::f32::consts::TAU / patch_count as f32;
        directions.push(Vec3::new(
            horizontal * azimuth.sin(),
            horizontal * azimuth.cos(),
            altitude.sin(),
        ));
    }
}
