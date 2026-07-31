pub mod reference;

#[cfg(target_os = "macos")]
pub mod metal;

pub use reference::ReferenceBackend;

#[cfg(target_os = "macos")]
pub use metal::MetalBackend;
