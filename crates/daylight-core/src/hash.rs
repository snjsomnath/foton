use bytemuck::bytes_of;

use crate::geometry::SceneData;

const FNV_OFFSET_BASIS: u64 = 0xcbf2_9ce4_8422_2325;
const FNV_PRIME: u64 = 0x0000_0100_0000_01b3;

pub fn scene_fingerprint(scene: &SceneData) -> u64 {
    let mut hash = FNV_OFFSET_BASIS;
    for vertex in &scene.vertices {
        update(&mut hash, bytes_of(vertex));
    }
    for triangle in &scene.triangles {
        for index in triangle {
            update(&mut hash, &index.to_le_bytes());
        }
    }
    for index in &scene.triangle_materials {
        update(&mut hash, &index.to_le_bytes());
    }
    for mesh in &scene.meshes {
        update(&mut hash, bytes_of(mesh));
    }
    for instance in &scene.instances {
        update(&mut hash, bytes_of(instance));
    }
    for material in &scene.materials {
        update(&mut hash, bytes_of(material));
    }
    for sensor in &scene.sensors {
        update(&mut hash, bytes_of(sensor));
    }
    hash
}

fn update(hash: &mut u64, bytes: &[u8]) {
    for byte in bytes {
        *hash ^= u64::from(*byte);
        *hash = hash.wrapping_mul(FNV_PRIME);
    }
}
