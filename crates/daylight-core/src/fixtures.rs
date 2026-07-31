use crate::{
    error::Result,
    geometry::{Instance, Material, MeshRange, SceneData, Sensor, Vec3},
};

pub const MASK_OPAQUE: u32 = 1 << 0;
pub const MASK_GLAZING: u32 = 1 << 1;
pub const MASK_EXTERIOR: u32 = 1 << 2;
pub const MASK_ACTIVE_BATCH: u32 = 1 << 3;

#[derive(Clone, Copy, Debug)]
pub struct ShoeboxOptions {
    pub room_count: usize,
    pub sensors_per_room: usize,
    pub glazing_transmittance: Option<[f32; 3]>,
}

impl Default for ShoeboxOptions {
    fn default() -> Self {
        Self {
            room_count: 1,
            sensors_per_room: 25,
            glazing_transmittance: None,
        }
    }
}

pub fn shoebox_scene(options: ShoeboxOptions) -> Result<SceneData> {
    let mut vertices = Vec::new();
    let mut triangles = Vec::new();
    let mut triangle_materials = Vec::new();

    add_quad(
        &mut vertices,
        &mut triangles,
        &mut triangle_materials,
        [
            Vec3::new(0.0, 0.0, 0.0),
            Vec3::new(6.0, 0.0, 0.0),
            Vec3::new(6.0, 9.0, 0.0),
            Vec3::new(0.0, 9.0, 0.0),
        ],
        1,
    );
    add_quad(
        &mut vertices,
        &mut triangles,
        &mut triangle_materials,
        [
            Vec3::new(0.0, 0.0, 3.0),
            Vec3::new(0.0, 9.0, 3.0),
            Vec3::new(6.0, 9.0, 3.0),
            Vec3::new(6.0, 0.0, 3.0),
        ],
        2,
    );
    add_quad(
        &mut vertices,
        &mut triangles,
        &mut triangle_materials,
        [
            Vec3::new(0.0, 0.0, 0.0),
            Vec3::new(0.0, 9.0, 0.0),
            Vec3::new(0.0, 9.0, 3.0),
            Vec3::new(0.0, 0.0, 3.0),
        ],
        0,
    );
    add_quad(
        &mut vertices,
        &mut triangles,
        &mut triangle_materials,
        [
            Vec3::new(6.0, 0.0, 0.0),
            Vec3::new(6.0, 0.0, 3.0),
            Vec3::new(6.0, 9.0, 3.0),
            Vec3::new(6.0, 9.0, 0.0),
        ],
        0,
    );
    add_quad(
        &mut vertices,
        &mut triangles,
        &mut triangle_materials,
        [
            Vec3::new(0.0, 9.0, 0.0),
            Vec3::new(6.0, 9.0, 0.0),
            Vec3::new(6.0, 9.0, 3.0),
            Vec3::new(0.0, 9.0, 3.0),
        ],
        0,
    );

    for quad in [
        [
            Vec3::new(0.0, 0.0, 0.0),
            Vec3::new(1.5, 0.0, 0.0),
            Vec3::new(1.5, 0.0, 3.0),
            Vec3::new(0.0, 0.0, 3.0),
        ],
        [
            Vec3::new(4.5, 0.0, 0.0),
            Vec3::new(6.0, 0.0, 0.0),
            Vec3::new(6.0, 0.0, 3.0),
            Vec3::new(4.5, 0.0, 3.0),
        ],
        [
            Vec3::new(1.5, 0.0, 0.0),
            Vec3::new(4.5, 0.0, 0.0),
            Vec3::new(4.5, 0.0, 1.0),
            Vec3::new(1.5, 0.0, 1.0),
        ],
        [
            Vec3::new(1.5, 0.0, 2.5),
            Vec3::new(4.5, 0.0, 2.5),
            Vec3::new(4.5, 0.0, 3.0),
            Vec3::new(1.5, 0.0, 3.0),
        ],
    ] {
        add_quad(
            &mut vertices,
            &mut triangles,
            &mut triangle_materials,
            quad,
            0,
        );
    }

    let mut materials = vec![
        Material::lambertian([0.7; 3]),
        Material::lambertian([0.2; 3]),
        Material::lambertian([0.8; 3]),
    ];
    if let Some(transmittance) = options.glazing_transmittance {
        let glass_index = materials.len() as u32;
        materials.push(Material::thin_glass(transmittance));
        add_quad(
            &mut vertices,
            &mut triangles,
            &mut triangle_materials,
            [
                Vec3::new(1.5, 0.0, 1.0),
                Vec3::new(4.5, 0.0, 1.0),
                Vec3::new(4.5, 0.0, 2.5),
                Vec3::new(1.5, 0.0, 2.5),
            ],
            glass_index,
        );
    }

    let triangle_count = triangles.len() as u32;
    let mut instances = Vec::with_capacity(options.room_count);
    let mut sensors = Vec::with_capacity(options.room_count * options.sensors_per_room);
    let room_columns = (options.room_count as f32).sqrt().ceil() as usize;
    for room_index in 0..options.room_count {
        let column = room_index % room_columns;
        let row = room_index / room_columns;
        let offset = Vec3::new(column as f32 * 8.0, row as f32 * 11.0, 0.0);
        let mut transform = Instance::default().transform;
        transform[3] = offset.x;
        transform[7] = offset.y;
        instances.push(Instance {
            transform,
            mesh_index: 0,
            room_id: room_index as u32,
            category_mask: MASK_OPAQUE | MASK_GLAZING | MASK_EXTERIOR | MASK_ACTIVE_BATCH,
            _padding: 0,
        });
        append_sensor_grid(&mut sensors, room_index, options.sensors_per_room, offset);
    }

    let mut scene = SceneData {
        vertices,
        triangles,
        triangle_materials,
        meshes: vec![MeshRange {
            first_triangle: 0,
            triangle_count,
        }],
        instances,
        materials,
        sensors,
    };
    scene.validate()?;
    Ok(scene)
}

fn append_sensor_grid(
    sensors: &mut Vec<Sensor>,
    room_index: usize,
    sensor_count: usize,
    offset: Vec3,
) {
    let columns = (sensor_count as f32).sqrt().ceil() as usize;
    let rows = sensor_count.div_ceil(columns);
    for local_index in 0..sensor_count {
        let column = local_index % columns;
        let row = local_index / columns;
        let x = (column + 1) as f32 * 6.0 / (columns + 1) as f32;
        let y = (row + 1) as f32 * 9.0 / (rows + 1) as f32;
        sensors.push(Sensor {
            position: Vec3::new(x + offset.x, y + offset.y, 0.75),
            normal: Vec3::new(0.0, 0.0, 1.0),
            sensor_id: (room_index * sensor_count + local_index) as u32,
            room_id: room_index as u32,
            area_weight: 54.0 / sensor_count as f32,
            _padding: [0; 3],
        });
    }
}

fn add_quad(
    vertices: &mut Vec<Vec3>,
    triangles: &mut Vec<[u32; 3]>,
    triangle_materials: &mut Vec<u32>,
    quad: [Vec3; 4],
    material_index: u32,
) {
    let first = vertices.len() as u32;
    vertices.extend(quad);
    triangles.push([first, first + 1, first + 2]);
    triangles.push([first, first + 2, first + 3]);
    triangle_materials.extend([material_index, material_index]);
}
