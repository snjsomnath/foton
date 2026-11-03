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
    // Evaluate in f64: the subtraction in the numerator loses too much
    // precision in f32 for the Radiance constants.
    let transmittance = f64::from(transmittance);
    let numerator = (0.840_252_843_5 + 0.007_252_223_9 * transmittance * transmittance).sqrt()
        - 0.916_653_066_1;
    Ok((numerator / (0.003_626_111_9 * transmittance)) as f32)
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
    Ok(thin_glass_optics(internal_transmissivity, cos_incident)?.0)
}

pub fn thin_glass_reflectance_from_transmissivity(
    internal_transmissivity: f32,
    cos_incident: f32,
) -> Result<f32> {
    Ok(thin_glass_optics(internal_transmissivity, cos_incident)?.1)
}

fn thin_glass_optics(internal_transmissivity: f32, cos_incident: f32) -> Result<(f32, f32)> {
    if !internal_transmissivity.is_finite()
        || !(0.0..=1.0).contains(&internal_transmissivity)
        || !cos_incident.is_finite()
        || !(0.0..=1.0).contains(&cos_incident.abs())
    {
        return Err(DaylightError::InvalidValue {
            field: "glass_transmissivity",
            detail: "transmissivity and incidence cosine must be finite and within [0, 1]".into(),
        });
    }
    let incident = cos_incident.abs();
    let index_squared = GLASS_INDEX_OF_REFRACTION * GLASS_INDEX_OF_REFRACTION;
    let transmitted = ((1.0 - 1.0 / index_squared) + incident * incident / index_squared).sqrt();
    let attenuation = internal_transmissivity.powf(1.0 / transmitted);

    // This is the exact non-refracting thin-glass equation used by Radiance
    // glass.c. The two terms are the perpendicular and parallel polarizations.
    let perpendicular = (incident - GLASS_INDEX_OF_REFRACTION * transmitted)
        / (incident + GLASS_INDEX_OF_REFRACTION * transmitted);
    let perpendicular_reflectance = perpendicular * perpendicular;
    let parallel = (transmitted - GLASS_INDEX_OF_REFRACTION * incident)
        / (transmitted + GLASS_INDEX_OF_REFRACTION * incident);
    let parallel_reflectance = parallel * parallel;
    let attenuation_squared = attenuation * attenuation;
    let perpendicular_transmission =
        (1.0 - perpendicular_reflectance) * (1.0 - perpendicular_reflectance) * attenuation
            / (1.0 - perpendicular_reflectance * perpendicular_reflectance * attenuation_squared);
    let parallel_transmission =
        (1.0 - parallel_reflectance) * (1.0 - parallel_reflectance) * attenuation
            / (1.0 - parallel_reflectance * parallel_reflectance * attenuation_squared);
    let perpendicular_reflection = perpendicular_reflectance
        * (1.0 + (1.0 - 2.0 * perpendicular_reflectance) * attenuation_squared)
        / (1.0 - perpendicular_reflectance * perpendicular_reflectance * attenuation_squared);
    let parallel_reflection = parallel_reflectance
        * (1.0 + (1.0 - 2.0 * parallel_reflectance) * attenuation_squared)
        / (1.0 - parallel_reflectance * parallel_reflectance * attenuation_squared);
    Ok((
        (0.5 * (perpendicular_transmission + parallel_transmission)).max(0.0),
        (0.5 * (perpendicular_reflection + parallel_reflection)).max(0.0),
    ))
}
