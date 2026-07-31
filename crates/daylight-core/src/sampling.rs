use serde::{Deserialize, Serialize};

use crate::geometry::Vec3;

#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub struct SampleKey {
    pub scene_seed: u64,
    pub sensor_id: u32,
    pub sample_index: u32,
    pub bounce_depth: u32,
    pub dimension: u32,
}

const SOBOL_PARAMETERS: &[(u32, u32, &[u32])] = &[
    (0, 0, &[]),
    (1, 0, &[1]),
    (2, 1, &[1, 3]),
    (3, 1, &[1, 3, 1]),
    (3, 2, &[1, 1, 1]),
    (4, 1, &[1, 3, 5, 13]),
    (4, 4, &[1, 1, 5, 5]),
    (5, 2, &[1, 3, 3, 9, 7]),
    (5, 4, &[1, 1, 3, 11, 13]),
    (5, 7, &[1, 1, 5, 1, 15]),
    (5, 11, &[1, 1, 7, 3, 11]),
    (5, 13, &[1, 3, 5, 5, 1]),
    (5, 14, &[1, 3, 7, 7, 9]),
    (6, 1, &[1, 3, 3, 9, 9, 27]),
    (6, 13, &[1, 1, 3, 3, 13, 7]),
    (6, 16, &[1, 3, 5, 11, 7, 11]),
];

pub fn low_discrepancy_sample(key: SampleKey) -> f32 {
    let dimension = key.dimension as usize % SOBOL_PARAMETERS.len();
    let sobol = sobol_uint(key.sample_index, dimension);
    let scramble_seed = mix32(
        key.scene_seed as u32
            ^ (key.scene_seed >> 32) as u32
            ^ key.sensor_id.rotate_left(7)
            ^ key.bounce_depth.rotate_left(13)
            ^ key.dimension.wrapping_mul(0x9e37_79b9),
    );
    let scrambled = owen_scramble(sobol, scramble_seed);
    ((scrambled as f64 + 0.5) / (u32::MAX as f64 + 1.0)) as f32
}

pub fn sobol_uint(index: u32, dimension: usize) -> u32 {
    let direction_numbers = direction_numbers(dimension % SOBOL_PARAMETERS.len());
    let gray_code = index ^ (index >> 1);
    let mut value = 0;
    for bit in 0..32 {
        if gray_code & (1 << bit) != 0 {
            value ^= direction_numbers[bit];
        }
    }
    value
}

pub fn cosine_hemisphere(first: f32, second: f32) -> Vec3 {
    let radius = first.clamp(0.0, 1.0).sqrt();
    let azimuth = std::f32::consts::TAU * second.clamp(0.0, 1.0);
    Vec3::new(
        radius * azimuth.cos(),
        radius * azimuth.sin(),
        (1.0 - first.clamp(0.0, 1.0)).sqrt(),
    )
}

fn direction_numbers(dimension: usize) -> [u32; 32] {
    let mut directions = [0_u32; 32];
    if dimension == 0 {
        for (bit, direction) in directions.iter_mut().enumerate() {
            *direction = 1 << (31 - bit);
        }
        return directions;
    }
    let (degree, coefficients, initial) = SOBOL_PARAMETERS[dimension];
    let degree = degree as usize;
    for bit in 1..=degree {
        directions[bit - 1] = initial[bit - 1] << (32 - bit);
    }
    for bit in (degree + 1)..=32 {
        let mut direction = directions[bit - degree - 1] ^ (directions[bit - degree - 1] >> degree);
        for coefficient_index in 1..degree {
            let coefficient_bit = degree - 1 - coefficient_index;
            if coefficients & (1 << coefficient_bit) != 0 {
                direction ^= directions[bit - coefficient_index - 1];
            }
        }
        directions[bit - 1] = direction;
    }
    directions
}

fn owen_scramble(mut value: u32, seed: u32) -> u32 {
    value = value.reverse_bits();
    value ^= value.wrapping_mul(0x3d20_adea);
    value = value.wrapping_add(seed);
    value = value.wrapping_mul((seed >> 16) | 1);
    value ^= value.wrapping_mul(0x0552_6c56);
    value ^= value.wrapping_mul(0x53a2_2864);
    value.reverse_bits()
}

fn mix32(mut value: u32) -> u32 {
    value ^= value >> 16;
    value = value.wrapping_mul(0x7feb_352d);
    value ^= value >> 15;
    value = value.wrapping_mul(0x846c_a68b);
    value ^ (value >> 16)
}
