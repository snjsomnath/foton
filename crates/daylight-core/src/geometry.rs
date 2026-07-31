use std::collections::HashSet;

use bytemuck::{Pod, Zeroable};
use serde::{Deserialize, Serialize};

use crate::error::{DaylightError, Result};

#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Pod, Zeroable, Serialize, Deserialize)]
pub struct Vec3 {
    pub x: f32,
    pub y: f32,
    pub z: f32,
}

impl Vec3 {
    pub const fn new(x: f32, y: f32, z: f32) -> Self {
        Self { x, y, z }
    }

    pub fn dot(self, other: Self) -> f32 {
        self.x * other.x + self.y * other.y + self.z * other.z
    }

    pub fn cross(self, other: Self) -> Self {
        Self::new(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )
    }

    pub fn add(self, other: Self) -> Self {
        Self::new(self.x + other.x, self.y + other.y, self.z + other.z)
    }

    pub fn subtract(self, other: Self) -> Self {
        Self::new(self.x - other.x, self.y - other.y, self.z - other.z)
    }

    pub fn scale(self, scale: f32) -> Self {
        Self::new(self.x * scale, self.y * scale, self.z * scale)
    }

    pub fn length(self) -> f32 {
        self.dot(self).sqrt()
    }

    pub fn normalized(self) -> Result<Self> {
        let length = self.length();
        if !length.is_finite() || length <= f32::EPSILON {
            return Err(DaylightError::InvalidValue {
                field: "normal",
                detail: "normal must be finite and non-zero".into(),
            });
        }
        Ok(Self::new(self.x / length, self.y / length, self.z / length))
    }

    pub fn normalized_or(self, fallback: Self) -> Self {
        let length = self.length();
        if length.is_finite() && length > f32::EPSILON {
            self.scale(length.recip())
        } else {
            fallback
        }
    }

    pub fn is_finite(self) -> bool {
        self.x.is_finite() && self.y.is_finite() && self.z.is_finite()
    }
}

#[repr(u32)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, Serialize, Deserialize)]
pub enum MaterialKind {
    #[default]
    Lambertian = 0,
    ThinGlass = 1,
}

#[repr(C)]
#[derive(Clone, Copy, Debug, PartialEq, Pod, Zeroable, Serialize, Deserialize)]
pub struct Material {
    pub kind: u32,
    pub diffuse_rgb: [f32; 3],
    pub transmittance_rgb: [f32; 3],
    pub internal_transmissivity_rgb: [f32; 3],
    pub _padding: u32,
}

impl Material {
    pub fn lambertian(diffuse_rgb: [f32; 3]) -> Self {
        Self {
            kind: MaterialKind::Lambertian as u32,
            diffuse_rgb,
            transmittance_rgb: [0.0; 3],
            internal_transmissivity_rgb: [0.0; 3],
            _padding: 0,
        }
    }

    pub fn thin_glass(transmittance_rgb: [f32; 3]) -> Self {
        Self {
            kind: MaterialKind::ThinGlass as u32,
            diffuse_rgb: [0.0; 3],
            transmittance_rgb,
            internal_transmissivity_rgb: [0.0; 3],
            _padding: 0,
        }
    }

    pub fn validate(&mut self) -> Result<()> {
        if self.kind > MaterialKind::ThinGlass as u32 {
            return Err(DaylightError::InvalidValue {
                field: "materials.kind",
                detail: format!("unknown material kind {}", self.kind),
            });
        }
        for (field, values) in [
            ("materials.diffuse_rgb", self.diffuse_rgb),
            ("materials.transmittance_rgb", self.transmittance_rgb),
        ] {
            if values
                .iter()
                .any(|value| !value.is_finite() || !(0.0..=1.0).contains(value))
            {
                return Err(DaylightError::InvalidValue {
                    field,
                    detail: "RGB values must be finite and within [0, 1]".into(),
                });
            }
        }
        self.internal_transmissivity_rgb = if self.kind == MaterialKind::ThinGlass as u32 {
            [
                crate::material::radiance_glass_transmissivity(self.transmittance_rgb[0])?,
                crate::material::radiance_glass_transmissivity(self.transmittance_rgb[1])?,
                crate::material::radiance_glass_transmissivity(self.transmittance_rgb[2])?,
            ]
        } else {
            [0.0; 3]
        };
        Ok(())
    }
}

#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, Pod, Zeroable, Serialize, Deserialize)]
pub struct MeshRange {
    pub first_triangle: u32,
    pub triangle_count: u32,
}

#[repr(C)]
#[derive(Clone, Copy, Debug, PartialEq, Pod, Zeroable, Serialize, Deserialize)]
pub struct Instance {
    pub transform: [f32; 16],
    pub mesh_index: u32,
    pub room_id: u32,
    pub category_mask: u32,
    pub _padding: u32,
}

impl Default for Instance {
    fn default() -> Self {
        Self {
            transform: [
                1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0,
            ],
            mesh_index: 0,
            room_id: 0,
            category_mask: u32::MAX,
            _padding: 0,
        }
    }
}

#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Pod, Zeroable, Serialize, Deserialize)]
pub struct Sensor {
    pub position: Vec3,
    pub normal: Vec3,
    pub sensor_id: u32,
    pub room_id: u32,
    pub area_weight: f32,
    pub _padding: [u32; 3],
}

#[derive(Clone, Debug, Default, Serialize, Deserialize)]
pub struct SceneData {
    pub vertices: Vec<Vec3>,
    pub triangles: Vec<[u32; 3]>,
    pub triangle_materials: Vec<u32>,
    pub meshes: Vec<MeshRange>,
    pub instances: Vec<Instance>,
    pub materials: Vec<Material>,
    pub sensors: Vec<Sensor>,
}

impl SceneData {
    pub fn validate(&mut self) -> Result<()> {
        if self.vertices.is_empty() || self.triangles.is_empty() {
            return Err(DaylightError::InvalidShape {
                field: "geometry",
                detail: "at least one vertex and triangle are required".into(),
            });
        }
        if self.triangle_materials.len() != self.triangles.len() {
            return Err(DaylightError::InvalidShape {
                field: "triangle_materials",
                detail: "must contain one material index per triangle".into(),
            });
        }
        if self.materials.is_empty() || self.sensors.is_empty() {
            return Err(DaylightError::InvalidShape {
                field: "scene",
                detail: "at least one material and sensor are required".into(),
            });
        }
        if self.vertices.iter().any(|vertex| !vertex.is_finite()) {
            return Err(DaylightError::InvalidValue {
                field: "vertices",
                detail: "vertices must be finite".into(),
            });
        }
        for triangle in &self.triangles {
            if triangle
                .iter()
                .any(|index| *index as usize >= self.vertices.len())
            {
                return Err(DaylightError::InvalidValue {
                    field: "triangles",
                    detail: "triangle index exceeds vertex count".into(),
                });
            }
        }
        for material in &mut self.materials {
            material.validate()?;
        }
        if self
            .triangle_materials
            .iter()
            .any(|index| *index as usize >= self.materials.len())
        {
            return Err(DaylightError::InvalidValue {
                field: "triangle_materials",
                detail: "material index exceeds material count".into(),
            });
        }
        for mesh in &self.meshes {
            let end = mesh.first_triangle as usize + mesh.triangle_count as usize;
            if mesh.triangle_count == 0 || end > self.triangles.len() {
                return Err(DaylightError::InvalidValue {
                    field: "meshes",
                    detail: "mesh triangle range is empty or out of bounds".into(),
                });
            }
        }
        for instance in &self.instances {
            if instance.mesh_index as usize >= self.meshes.len() {
                return Err(DaylightError::InvalidValue {
                    field: "instances.mesh_index",
                    detail: "mesh index exceeds mesh count".into(),
                });
            }
            if instance.transform.iter().any(|value| !value.is_finite()) {
                return Err(DaylightError::InvalidValue {
                    field: "instances.transform",
                    detail: "transform values must be finite".into(),
                });
            }
        }
        let mut sensor_ids = HashSet::with_capacity(self.sensors.len());
        for sensor in &mut self.sensors {
            if !sensor.position.is_finite()
                || !sensor.area_weight.is_finite()
                || sensor.area_weight <= 0.0
            {
                return Err(DaylightError::InvalidValue {
                    field: "sensors",
                    detail: "positions must be finite and area weights positive".into(),
                });
            }
            sensor.normal = sensor.normal.normalized()?;
            if !sensor_ids.insert(sensor.sensor_id) {
                return Err(DaylightError::InvalidValue {
                    field: "sensors.sensor_id",
                    detail: format!("duplicate stable sensor ID {}", sensor.sensor_id),
                });
            }
        }
        Ok(())
    }
}
