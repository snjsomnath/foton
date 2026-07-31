use crate::error::{DaylightError, Result};

const GLASS_INDEX_OF_REFRACTION: f32 = 1.52;

pub fn radiance_glass_transmissivity(transmittance: f32) -> Result<f32> {
    if !transmittance.is_finite() || !(0.0..=1.0).contains(&transmittance) {
        return Err(DaylightError::InvalidValue {
            field: "visible_transmittance",
            detail: "must be finite and within [0, 1]".into(),
        });
    }
    if transmittance == 0.0 {
        return Ok(0.0);
    }
    let numerator =
        (0.840_252_8 + 0.007_252_224 * transmittance * transmittance).sqrt() - 0.916_653_1;
    Ok(numerator / (0.003_626_112 * transmittance))
}

pub fn fresnel_reflectance(cos_incident: f32, index_of_refraction: f32) -> Result<f32> {
    if !cos_incident.is_finite()
        || !(0.0..=1.0).contains(&cos_incident)
        || !index_of_refraction.is_finite()
        || index_of_refraction <= 0.0
    {
        return Err(DaylightError::InvalidValue {
            field: "fresnel",
            detail: "cosine must be within [0, 1] and refractive index positive".into(),
        });
    }
    let sin_incident_squared = (1.0 - cos_incident * cos_incident).max(0.0);
    let sin_transmitted_squared =
        sin_incident_squared / (index_of_refraction * index_of_refraction);
    if sin_transmitted_squared >= 1.0 {
        return Ok(1.0);
    }
    let cos_transmitted = (1.0 - sin_transmitted_squared).sqrt();
    let perpendicular = (cos_incident - index_of_refraction * cos_transmitted)
        / (cos_incident + index_of_refraction * cos_transmitted);
    let parallel = (index_of_refraction * cos_incident - cos_transmitted)
        / (index_of_refraction * cos_incident + cos_transmitted);
    Ok(0.5 * (perpendicular * perpendicular + parallel * parallel))
}

pub fn thin_glass_transmittance(visible_transmittance: f32, cos_incident: f32) -> Result<f32> {
    let internal_transmissivity = radiance_glass_transmissivity(visible_transmittance)?;
    thin_glass_transmittance_from_transmissivity(internal_transmissivity, cos_incident)
}

pub fn thin_glass_transmittance_from_transmissivity(
    internal_transmissivity: f32,
    cos_incident: f32,
) -> Result<f32> {
    if !internal_transmissivity.is_finite() || !(0.0..=1.0).contains(&internal_transmissivity) {
        return Err(DaylightError::InvalidValue {
            field: "glass_transmissivity",
            detail: "must be finite and within [0, 1]".into(),
        });
    }
    if internal_transmissivity == 0.0 {
        return Ok(0.0);
    }
    let reflectance = fresnel_reflectance(cos_incident.abs(), GLASS_INDEX_OF_REFRACTION)?;
    let interface_transmission = 1.0 - reflectance;
    let numerator = interface_transmission * interface_transmission * internal_transmissivity;
    let denominator =
        1.0 - reflectance * reflectance * internal_transmissivity * internal_transmissivity;
    Ok((numerator / denominator).max(0.0))
}
