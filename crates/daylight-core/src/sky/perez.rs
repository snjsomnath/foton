//! Foton's own all-weather sky matrix.
//!
//! This module turns a year of hourly direct-normal and diffuse-horizontal
//! irradiance (what a WEA file holds) into the per-patch sky radiance matrix
//! that the daylight-coefficient method consumes, so an annual analysis no
//! longer needs Radiance's `gendaymtx` at run time.
//!
//! The model is implemented from the published papers:
//!
//! * R. Perez, R. Seals and J. Michalsky, "All-weather model for sky luminance
//!   distribution - preliminary configuration and validation", *Solar Energy*
//!   50(3), 235-245, 1993 (and the erratum in 51(5), 423): the relative
//!   luminance function (eq. 1), the clearness bins and the coefficient table
//!   (Table 1) with the eqs. 6-8 parameter fits.
//! * R. Perez, P. Ineichen, R. Seals, J. Michalsky and R. Stewart, "Modeling
//!   daylight availability and irradiance components from direct and global
//!   irradiance", *Solar Energy* 44(5), 271-289, 1990: sky clearness (eq. 1),
//!   sky brightness (eq. 2), precipitable water (eq. 3) and the diffuse and
//!   direct luminous-efficacy fits (eqs. 7-8, Table 4) that convert the
//!   radiometric WEA inputs to the photometric quantities the matrix carries.
//! * F. Kasten, "A new table and approximation formula for the relative
//!   optical air mass", *Arch. Meteorol. Geophys. Bioklimatol.* B14, 206-223,
//!   1966: relative air mass.
//! * J. W. Spencer, "Fourier series representation of the position of the
//!   sun", *Search* 2(5), 172, 1971: the earth-orbit eccentricity correction.
//! * P. R. Tregenza, "Subdivision of the sky hemisphere for luminance
//!   measurements", *Lighting Research & Technology* 19(1), 13-14, 1987, and
//!   D. Bourgeois, C. F. Reinhart and G. Ward, "Standard daylight coefficient
//!   model for dynamic daylighting simulations", *Building Research &
//!   Information* 36(1), 68-82, 2008: the 145 + 1 patch subdivision and its
//!   Reinhart refinement, shared with the rest of Foton through
//!   [`SkyBasis`] and the ring table in the parent module.
//! * P. I. Cooper, "The absorption of radiation in solar stills", *Solar
//!   Energy* 12(3), 333-346, 1969: the solar declination approximation. The
//!   two-term sinusoidal equation of time and the local-standard-time to
//!   solar-time convention are those of Radiance's `gensky`/`gendaymtx`
//!   (G. Ward, 1987), adopted so that every hour is evaluated at the same
//!   solar position as the validation oracle.
//!
//! Radiance's `gendaymtx` is the validation oracle for this module, not its
//! source: `tests/python/test_builtin_sky.py` compares the matrix with
//! `gendaymtx -O0` for three climates at both patch densities. The
//! conventions needed for that comparison to agree to floating-point level
//! are documented where they appear: the default sky and ground colour
//! coefficients, the 179 lm/W luminous efficacy of equal-energy white, the
//! 11 degC default dew point used when a weather tape carries none, the
//! clamping of clearness and brightness (Radiance 5.4a, the validated
//! release, applies no upper brightness limit; Radiance 6 caps it at 0.6,
//! available through [`AllWeatherSkyOptions::max_brightness`]), the
//! half-sun-diameter sun-up rule, single-precision storage of the patch
//! table and of the relative luminances, the quarter-wave cosine table
//! Radiance uses in the dome integral that normalises the sky, and the
//! distribution of the direct component over the four patches nearest the
//! sun weighted by `1 / (1.002 - cos)`.

use super::{SkyBasis, SkyMatrix, TREGENZA_RING_COUNTS};
use crate::error::{DaylightError, Result};

/// Luminous efficacy of equal-energy white light in lm/W, the constant
/// Radiance uses to convert between photometric and radiometric units.
pub const WHITE_EFFICACY: f64 = 179.0;
/// Solar constant in W/m^2 used by the Perez brightness index.
pub const SOLAR_CONSTANT: f64 = 1367.0;
/// Full angular diameter of the solar disc in degrees.
pub const SUN_DIAMETER_DEGREES: f64 = 0.533;
/// Default sky colour multipliers (red, green, blue); their photometric
/// brightness is one so the sky stays energy-balanced.
pub const DEFAULT_SKY_COLOR: [f32; 3] = [0.96, 1.004, 1.118];
/// Default ground reflectance, a 20 % grey.
pub const DEFAULT_GROUND_REFLECTANCE: [f32; 3] = [0.2, 0.2, 0.2];
/// Dew point assumed when the weather input carries none, in degC.
pub const DEFAULT_DEW_POINT_CELSIUS: f64 = 11.0;
/// Number of patches the direct component is spread into.
const SUN_PATCH_COUNT: usize = 4;
/// Combined direct-plus-diffuse irradiance below which an hour is night.
const NIGHT_IRRADIANCE: f64 = 1e-4;
/// Radiance's `FTINY`: a relative horizontal illuminance below this is a
/// numerically empty sky and is replaced by a uniform one.
const TINY: f64 = 1e-6;

/// Perez et al. 1993, Table 1: for each of the eight clearness bins the four
/// fit coefficients of the five luminance parameters a, b, c, d, e, in the
/// order a1..a4, b1..b4, c1..c4, d1..d4, e1..e4.
const PEREZ_1993_TABLE_1: [[f64; 20]; 8] = [
    [
        1.3525, -0.2576, -0.2690, -1.4366, -0.7670, 0.0007, 1.2734, -0.1233, 2.8000, 0.6004,
        1.2375, 1.0000, 1.8734, 0.6297, 0.9738, 0.2809, 0.0356, -0.1246, -0.5718, 0.9938,
    ],
    [
        -1.2219, -0.7730, 1.4148, 1.1016, -0.2054, 0.0367, -3.9128, 0.9156, 6.9750, 0.1774, 6.4477,
        -0.1239, -1.5798, -0.5081, -1.7812, 0.1080, 0.2624, 0.0672, -0.2190, -0.4285,
    ],
    [
        -1.1000, -0.2515, 0.8952, 0.0156, 0.2782, -0.1812, -4.5000, 1.1766, 24.7219, -13.0812,
        -37.7000, 34.8438, -5.0000, 1.5218, 3.9229, -2.6204, -0.0156, 0.1597, 0.4199, -0.5562,
    ],
    [
        -0.5484, -0.6654, -0.2672, 0.7117, 0.7234, -0.6219, -5.6812, 2.6297, 33.3389, -18.3000,
        -62.2500, 52.0781, -3.5000, 0.0016, 1.1477, 0.1062, 0.4659, -0.3296, -0.0876, -0.0329,
    ],
    [
        -0.6000, -0.3566, -2.5000, 2.3250, 0.2937, 0.0496, -5.6812, 1.8415, 21.0000, -4.7656,
        -21.5906, 7.2492, -3.5000, -0.1554, 1.4062, 0.3988, 0.0032, 0.0766, -0.0656, -0.1294,
    ],
    [
        -1.0156, -0.3670, 1.0078, 1.4051, 0.2875, -0.5328, -3.8500, 3.3750, 14.0000, -0.9999,
        -7.1406, 7.5469, -3.4000, -0.1078, -1.0750, 1.5702, -0.0672, 0.4016, 0.3017, -0.4844,
    ],
    [
        -1.0000, 0.0211, 0.5025, -0.5119, -0.3000, 0.1922, 0.7023, -1.6317, 19.0000, -5.0000,
        1.2438, -1.9094, -4.0000, 0.0250, 0.3844, 0.2656, 1.0468, -0.3788, -2.4517, 1.4656,
    ],
    [
        -1.0500, 0.0289, 0.4260, 0.3590, -0.3250, 0.1156, 0.7781, 0.0025, 31.0625, -14.5000,
        -46.1148, 55.3750, -7.2312, 0.4050, 13.3500, 0.6234, 1.5000, -0.6426, 1.8564, 0.5636,
    ],
];

/// Lower bounds of the eight sky-clearness bins (Perez et al. 1990, Table 1);
/// the last bin is open above 6.2.
const CLEARNESS_BIN_LOWER_BOUNDS: [f64; 8] = [1.0, 1.065, 1.23, 1.5, 1.95, 2.8, 4.5, 6.2];

/// Perez et al. 1990, Table 4: diffuse luminous efficacy fit (eq. 7)
/// coefficients a, b, c, d per clearness bin.
const DIFFUSE_EFFICACY: [[f64; 4]; 8] = [
    [97.24, -0.46, 12.00, -8.91],
    [107.22, 1.15, 0.59, -3.95],
    [104.97, 2.96, -5.53, -8.77],
    [102.39, 5.59, -13.95, -13.90],
    [100.71, 5.94, -22.75, -23.74],
    [106.42, 3.83, -36.15, -28.83],
    [141.88, 1.90, -53.24, -14.03],
    [152.23, 0.35, -45.27, -7.98],
];

/// Perez et al. 1990, Table 4: direct luminous efficacy fit (eq. 8)
/// coefficients a, b, c, d per clearness bin.
const DIRECT_EFFICACY: [[f64; 4]; 8] = [
    [57.20, -4.55, -2.98, 117.12],
    [98.99, -3.46, -1.21, 12.38],
    [109.83, -4.90, -1.71, -8.81],
    [110.34, -5.84, -1.99, -4.56],
    [106.36, -3.97, -1.75, -6.16],
    [107.19, -1.25, -1.51, -26.73],
    [105.75, 0.77, -1.26, -34.44],
    [101.18, 1.58, -1.10, -8.29],
];

/// Where the weather was measured, in the EPW sign conventions.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct SkySite {
    /// Degrees north of the equator.
    pub latitude_degrees: f64,
    /// Degrees east of Greenwich (negative in the Americas).
    pub longitude_degrees: f64,
    /// Hours ahead of UTC for the standard meridian of the local clock.
    pub time_zone_hours: f64,
}

/// One weather time step: when it is and what the sky delivered.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct SkyStep {
    /// Day of the year, 1 for 1 January.
    pub day_of_year: u32,
    /// Local standard decimal hour; an hourly tape centres its steps at 0.5.
    pub hour: f64,
    /// Direct normal irradiance in W/m^2.
    pub direct_normal: f32,
    /// Diffuse horizontal irradiance in W/m^2.
    pub diffuse_horizontal: f32,
}

/// Which quantity the matrix carries per channel.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum SkyOutput {
    /// Visible radiance in W/sr/m^2 of equal-energy white (`gendaymtx -O0`).
    Visible,
    /// Total solar radiance in W/sr/m^2 (`gendaymtx -O1`).
    Solar,
}

/// Model options; [`AllWeatherSkyOptions::default`] reproduces `gendaymtx`'s
/// defaults for a Tregenza sky with north along +Y.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct AllWeatherSkyOptions {
    pub basis: SkyBasis,
    pub output: SkyOutput,
    /// Degrees the sky is rotated counter-clockwise about the zenith (west
    /// of north), the `-r` convention.
    pub north_degrees: f64,
    pub sky_color: [f32; 3],
    pub ground_reflectance: [f32; 3],
    pub dew_point_celsius: f64,
    /// Upper limit applied to the Perez brightness index, if any. Radiance
    /// 5.4a applies none (the validated oracle); Radiance 6 caps it at 0.6,
    /// which only changes low-sun hours with a large diffuse component.
    pub max_brightness: Option<f64>,
    /// Weight the dome integral that normalises the sky with Radiance's
    /// quarter-wave cosine table (1024 entries, nearest entry) instead of
    /// the exact sine of each patch altitude. `gendaymtx` evaluates that
    /// integral through its `tsin` table, which moves the whole dome's scale
    /// by up to 0.06 %; matching it keeps the matrix at floating-point
    /// agreement with the oracle. Exact sines are one flag away.
    pub oracle_cosine_table: bool,
}

impl Default for AllWeatherSkyOptions {
    fn default() -> Self {
        Self {
            basis: SkyBasis::Tregenza,
            output: SkyOutput::Visible,
            north_degrees: 0.0,
            sky_color: DEFAULT_SKY_COLOR,
            ground_reflectance: DEFAULT_GROUND_REFLECTANCE,
            dew_point_celsius: DEFAULT_DEW_POINT_CELSIUS,
            max_brightness: None,
            oracle_cosine_table: true,
        }
    }
}

/// Radiance's table cosine: the quarter wave sampled at 1024 steps, read at
/// the nearest entry after folding the angle into the first quadrant.
fn table_cosine(angle: f64) -> f64 {
    use std::f64::consts::PI;
    const ENTRIES: usize = 1024;
    let mut index = ((ENTRIES as f64 * 2.0 / PI) * angle.abs() + 0.5) as usize;
    index %= 4 * ENTRIES;
    let (sign, folded) = match index / ENTRIES {
        0 => (1.0, index),
        1 => (-1.0, 2 * ENTRIES - index),
        2 => (-1.0, index - 2 * ENTRIES),
        _ => (1.0, 4 * ENTRIES - index),
    };
    sign * ((PI / 2.0 / ENTRIES as f64) * folded as f64).cos()
}

/// Radiance's table sine, `tcos(x - pi/2)`.
fn table_sine(angle: f64) -> f64 {
    table_cosine(angle - std::f64::consts::FRAC_PI_2)
}

/// Sun position for one step, in the sky-matrix frame (+Y north, +X east).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct SolarPosition {
    /// Radians above the horizon (negative at night).
    pub altitude: f64,
    /// Radians clockwise from north after the `north_degrees` rotation.
    pub azimuth: f64,
}

impl SolarPosition {
    /// Unit vector towards the sun.
    pub fn direction(self) -> [f64; 3] {
        let horizontal = self.altitude.cos();
        [
            horizontal * self.azimuth.sin(),
            horizontal * self.azimuth.cos(),
            self.altitude.sin(),
        ]
    }

    /// Whether any part of the solar disc is above the horizon.
    pub fn sun_up(self) -> bool {
        self.altitude > -(SUN_DIAMETER_DEGREES / 2.0).to_radians()
    }
}

/// The annual matrix and the per-step facts an annual run needs next to it.
#[derive(Clone, Debug, PartialEq)]
pub struct AllWeatherSkyMatrix {
    /// Patch-major RGB radiance, `values[patch * steps + step]`, ground first.
    pub matrix: SkyMatrix,
    /// Steps with any part of the solar disc above the horizon.
    pub sun_up: Vec<bool>,
    pub solar_positions: Vec<SolarPosition>,
}

/// Solar declination, equation of time and position for one step.
///
/// Declination follows Cooper (1969); the equation of time is the two-term
/// sine approximation Radiance's `gensky` has used since 1987, with the
/// standard-meridian correction folded in. Altitude and azimuth come from
/// the usual spherical-triangle relations with the hour angle measured from
/// solar noon.
pub fn solar_position(
    site: &SkySite,
    day_of_year: u32,
    hour: f64,
    north_degrees: f64,
) -> SolarPosition {
    use std::f64::consts::PI;
    let day = day_of_year as f64;
    let latitude = site.latitude_degrees.to_radians();
    // Radiance measures longitude and meridian west-positive.
    let longitude_west = -site.longitude_degrees.to_radians();
    let meridian_west = -(15.0 * site.time_zone_hours).to_radians();
    let declination = 0.4093 * ((2.0 * PI / 365.0) * (day - 81.0)).sin();
    let time_adjustment = 0.170 * ((4.0 * PI / 373.0) * (day - 80.0)).sin()
        - 0.129 * ((2.0 * PI / 355.0) * (day - 8.0)).sin()
        + (12.0 / PI) * (meridian_west - longitude_west);
    let solar_time = hour + time_adjustment;
    let hour_angle = solar_time * (PI / 12.0);
    let altitude = (latitude.sin() * declination.sin()
        - latitude.cos() * declination.cos() * hour_angle.cos())
    .asin();
    let azimuth_from_south = -(declination.cos() * hour_angle.sin()).atan2(
        -latitude.cos() * declination.sin() - latitude.sin() * declination.cos() * hour_angle.cos(),
    );
    SolarPosition {
        altitude,
        azimuth: azimuth_from_south + PI - north_degrees.to_radians(),
    }
}

/// Centre altitude, centre azimuth and solid angle of every patch, ground
/// first and zenith last, stored in single precision like the matrix itself.
#[derive(Clone, Debug, PartialEq)]
pub struct PatchTable {
    pub altitude: Vec<f32>,
    pub azimuth: Vec<f32>,
    pub solid_angle: Vec<f32>,
}

impl PatchTable {
    /// Tregenza's 145-patch dome (plus ground) or its Reinhart subdivision:
    /// equal-height rings of `12 / M` degrees, a polar cap half a ring tall,
    /// and ring `r` split into `M` times the Tregenza count azimuthally.
    pub fn new(basis: SkyBasis) -> Self {
        use std::f64::consts::PI;
        let multiplier = match basis {
            SkyBasis::Tregenza => 1,
            SkyBasis::ReinhartMf2 => 2,
        };
        let row_count = TREGENZA_RING_COUNTS.len() * multiplier;
        let ring_height = (PI / 2.0) / (row_count as f64 + 0.5);
        let patch_count = basis.row_count();
        let mut altitude = Vec::with_capacity(patch_count);
        let mut azimuth = Vec::with_capacity(patch_count);
        let mut solid_angle = Vec::with_capacity(patch_count);
        altitude.push((-PI / 2.0) as f32);
        azimuth.push(0.0);
        solid_angle.push((2.0 * PI) as f32);
        for row in 0..row_count {
            let row_altitude = (ring_height * (row as f64 + 0.5)) as f32;
            let in_row = TREGENZA_RING_COUNTS[row / multiplier] * multiplier;
            let row_solid_angle = (2.0
                * PI
                * ((ring_height * (row as f64 + 1.0)).sin() - (ring_height * row as f64).sin())
                / in_row as f64) as f32;
            for index in 0..in_row {
                altitude.push(row_altitude);
                azimuth.push((2.0 * PI * index as f64 / in_row as f64) as f32);
                solid_angle.push(row_solid_angle);
            }
        }
        altitude.push((PI / 2.0) as f32);
        azimuth.push(0.0);
        solid_angle.push((2.0 * PI * (1.0 - (ring_height * 0.5).cos())) as f32);
        debug_assert_eq!(altitude.len(), patch_count);
        Self {
            altitude,
            azimuth,
            solid_angle,
        }
    }

    pub fn len(&self) -> usize {
        self.altitude.len()
    }

    pub fn is_empty(&self) -> bool {
        self.altitude.is_empty()
    }

    fn direction(&self, patch: usize) -> [f64; 3] {
        let altitude = self.altitude[patch] as f64;
        let azimuth = self.azimuth[patch] as f64;
        let horizontal = altitude.cos();
        [
            horizontal * azimuth.sin(),
            horizontal * azimuth.cos(),
            altitude.sin(),
        ]
    }
}

/// Build the annual sky matrix for every step.
///
/// The result has `basis.row_count()` patches times `steps.len()` columns;
/// a step whose direct plus diffuse irradiance is below 0.1 W/m^2 is a black
/// column. Nothing is allocated beyond the output and one scratch row.
pub fn all_weather_sky_matrix(
    site: &SkySite,
    steps: &[SkyStep],
    options: &AllWeatherSkyOptions,
) -> Result<AllWeatherSkyMatrix> {
    if steps.is_empty() {
        return Err(DaylightError::InvalidShape {
            field: "steps",
            detail: "at least one weather step is required".into(),
        });
    }
    for value in [
        site.latitude_degrees,
        site.longitude_degrees,
        site.time_zone_hours,
    ] {
        if !value.is_finite() {
            return Err(DaylightError::InvalidValue {
                field: "site",
                detail: "latitude, longitude and time zone must be finite".into(),
            });
        }
    }
    if !(-90.0..=90.0).contains(&site.latitude_degrees) {
        return Err(DaylightError::InvalidValue {
            field: "site",
            detail: "latitude must lie between -90 and 90 degrees".into(),
        });
    }
    if !options.north_degrees.is_finite()
        || !options.dew_point_celsius.is_finite()
        || options
            .max_brightness
            .is_some_and(|limit| limit.is_nan() || limit <= 0.0)
    {
        return Err(DaylightError::InvalidValue {
            field: "options",
            detail: "north and dew point must be finite and max_brightness positive".into(),
        });
    }
    for step in steps {
        if step.day_of_year == 0 || step.day_of_year > 366 || !step.hour.is_finite() {
            return Err(DaylightError::InvalidValue {
                field: "steps",
                detail: "day_of_year must be 1..=366 and hour finite".into(),
            });
        }
        if !step.direct_normal.is_finite()
            || !step.diffuse_horizontal.is_finite()
            || step.direct_normal < 0.0
            || step.diffuse_horizontal < 0.0
        {
            return Err(DaylightError::InvalidValue {
                field: "steps",
                detail: "irradiances must be finite and non-negative".into(),
            });
        }
    }

    let patches = PatchTable::new(options.basis);
    let patch_count = patches.len();
    let step_count = steps.len();
    let mut values = vec![[0.0f32; 3]; patch_count * step_count];
    let mut column = vec![[0.0f32; 3]; patch_count];
    let mut sun_up = Vec::with_capacity(step_count);
    let mut solar_positions = Vec::with_capacity(step_count);
    let precipitable_water = (0.07 * options.dew_point_celsius - 0.075).exp();

    for (step_index, step) in steps.iter().enumerate() {
        let sun = solar_position(site, step.day_of_year, step.hour, options.north_degrees);
        sun_up.push(sun.sun_up());
        solar_positions.push(sun);
        let direct = step.direct_normal as f64;
        let diffuse = step.diffuse_horizontal as f64;
        if direct + diffuse <= NIGHT_IRRADIANCE {
            continue;
        }
        compute_column(
            &patches,
            &sun,
            step.day_of_year,
            direct,
            diffuse,
            precipitable_water,
            options,
            &mut column,
        );
        for (patch, value) in column.iter().enumerate() {
            values[patch * step_count + step_index] = *value;
        }
    }

    Ok(AllWeatherSkyMatrix {
        matrix: SkyMatrix::new(options.basis, step_count, values)?,
        sun_up,
        solar_positions,
    })
}

#[allow(clippy::too_many_arguments)]
fn compute_column(
    patches: &PatchTable,
    sun: &SolarPosition,
    day_of_year: u32,
    direct_irradiance: f64,
    diffuse_irradiance: f64,
    precipitable_water: f64,
    options: &AllWeatherSkyOptions,
    column: &mut [[f32; 3]],
) {
    use std::f64::consts::PI;
    // The sun zenith angle used by the luminance model is kept on or above
    // the horizon and at least 3 degrees from the zenith so the circumsolar
    // term stays finite.
    let sun_zenith = if sun.altitude <= 0.0 {
        90.0_f64.to_radians()
    } else if sun.altitude >= 87.0_f64.to_radians() {
        3.0_f64.to_radians()
    } else {
        90.0_f64.to_radians() - sun.altitude
    };
    // Kasten (1966) relative air mass and Spencer (1971) eccentricity.
    let air_mass =
        1.0 / (sun_zenith.cos() + 0.15 * (93.885 - sun_zenith.to_degrees()).powf(-1.253));
    let day_angle = (day_of_year as f64 - 1.0) * (2.0 * PI / 365.0);
    let eccentricity = 1.00011
        + 0.034221 * day_angle.cos()
        + 0.00128 * day_angle.sin()
        + 0.000719 * (2.0 * day_angle).cos()
        + 0.000077 * (2.0 * day_angle).sin();
    // Perez 1990 eqs. 2 and 1, kept inside the fitted ranges: brightness at
    // least 0.01 and clearness at most 11.9 (it cannot fall below 1 for
    // non-negative irradiances); an upper brightness limit is optional.
    let mut brightness =
        (diffuse_irradiance * air_mass / (SOLAR_CONSTANT * eccentricity)).max(0.01);
    if let Some(limit) = options.max_brightness {
        brightness = brightness.min(limit);
    }
    let zenith_cubed = sun_zenith * sun_zenith * sun_zenith;
    let clearness = (((diffuse_irradiance + direct_irradiance) / diffuse_irradiance
        + 1.041 * zenith_cubed)
        / (1.0 + 1.041 * zenith_cubed))
        .min(11.9);
    let bin = clearness_bin(clearness);

    // Perez 1990 eqs. 7-8: luminous efficacies turn the irradiances into the
    // photometric quantities the sky is normalised to.
    let (diffuse_illuminance, direct_illuminance) = match options.output {
        SkyOutput::Visible => {
            let diffuse_coefficients = DIFFUSE_EFFICACY[bin];
            let direct_coefficients = DIRECT_EFFICACY[bin];
            let diffuse_efficacy = diffuse_coefficients[0]
                + diffuse_coefficients[1] * precipitable_water
                + diffuse_coefficients[2] * sun_zenith.cos()
                + diffuse_coefficients[3] * brightness.ln();
            let direct_efficacy = (direct_coefficients[0]
                + direct_coefficients[1] * precipitable_water
                + direct_coefficients[2] * (5.73 * sun_zenith - 5.0).exp()
                + direct_coefficients[3] * brightness)
                .max(0.0);
            (
                diffuse_irradiance * diffuse_efficacy,
                direct_irradiance * direct_efficacy,
            )
        }
        SkyOutput::Solar => (
            diffuse_irradiance * WHITE_EFFICACY,
            direct_irradiance * WHITE_EFFICACY,
        ),
    };

    // Ground patch: horizontal illuminance reflected by a Lambertian ground.
    let mut ground = diffuse_illuminance as f32;
    if sun.altitude > 0.0 {
        ground = (ground as f64 + direct_illuminance * sun.altitude.sin()) as f32;
    }
    ground = (ground as f64 * (1.0 / PI / WHITE_EFFICACY)) as f32;
    for (value, reflectance) in column[0].iter_mut().zip(options.ground_reflectance) {
        *value = ground * reflectance;
    }

    // Perez 1993 eq. 1 over the dome, relative to the zenith.
    let parameters = perez_parameters(sun_zenith, clearness, brightness, bin);
    let patch_count = patches.len();
    let mut relative_horizontal = 0.0f64;
    for (patch, value) in column.iter_mut().enumerate().take(patch_count).skip(1) {
        let patch_zenith = PI * 0.5 - patches.altitude[patch] as f64;
        let azimuth_difference = (patches.azimuth[patch] as f64 - sun.azimuth).abs();
        let sun_patch_angle = (sun_zenith.cos() * patch_zenith.cos()
            + sun_zenith.sin() * patch_zenith.sin() * azimuth_difference.cos())
        .acos();
        let luminance =
            (relative_luminance(&parameters, sun_patch_angle, patch_zenith) as f32).max(0.0);
        *value = [luminance; 3];
        let altitude = patches.altitude[patch] as f64;
        let cosine = if options.oracle_cosine_table {
            table_sine(altitude)
        } else {
            altitude.sin()
        };
        relative_horizontal += luminance as f64 * cosine * patches.solid_angle[patch] as f64;
    }
    if relative_horizontal <= TINY {
        for value in column.iter_mut().skip(1) {
            *value = [1.0; 3];
        }
        relative_horizontal = PI;
    }
    // Perez 1993 eq. 3: scale so the dome integrates to the measured diffuse
    // horizontal illuminance, then express the result as radiance.
    let scale = diffuse_illuminance / relative_horizontal * (1.0 / WHITE_EFFICACY);
    for value in column.iter_mut().skip(1) {
        for (channel, color) in value.iter_mut().zip(options.sky_color) {
            *channel = (*channel as f64 * scale) as f32 * color;
        }
    }

    add_direct(patches, sun, direct_illuminance, column);
}

/// Spread the direct component over the four patches whose centres are
/// nearest the sun, weighted by `1 / (1.002 - cos)` of the angle between
/// them, as `gendaymtx` does for a two-phase matrix.
fn add_direct(
    patches: &PatchTable,
    sun: &SolarPosition,
    direct_illuminance: f64,
    column: &mut [[f32; 3]],
) {
    if direct_illuminance <= 1e-4 {
        return;
    }
    let sun_direction = sun.direction();
    let mut nearest_cosines = [-1.0f64; SUN_PATCH_COUNT];
    let mut nearest_patches = [0usize; SUN_PATCH_COUNT];
    for patch in 1..patches.len() {
        let direction = patches.direction(patch);
        let cosine = direction[0] * sun_direction[0]
            + direction[1] * sun_direction[1]
            + direction[2] * sun_direction[2];
        if let Some(slot) = nearest_cosines.iter().position(|&kept| cosine > kept) {
            for later in (slot + 1..SUN_PATCH_COUNT).rev() {
                nearest_cosines[later] = nearest_cosines[later - 1];
                nearest_patches[later] = nearest_patches[later - 1];
            }
            nearest_cosines[slot] = cosine;
            nearest_patches[slot] = patch;
        }
    }
    let mut weights = [0.0f64; SUN_PATCH_COUNT];
    let mut weight_total = 0.0f64;
    for slot in (0..SUN_PATCH_COUNT).rev() {
        weights[slot] = 1.0 / (1.002 - nearest_cosines[slot]);
        weight_total += weights[slot];
    }
    for slot in (0..SUN_PATCH_COUNT).rev() {
        let patch = nearest_patches[slot];
        let mut added =
            (weights[slot] * direct_illuminance / (WHITE_EFFICACY * weight_total)) as f32;
        added /= patches.solid_angle[patch];
        for channel in column[patch].iter_mut() {
            *channel += added;
        }
    }
}

/// Index of the clearness bin of Perez et al. 1990, Table 1.
pub fn clearness_bin(clearness: f64) -> usize {
    CLEARNESS_BIN_LOWER_BOUNDS
        .iter()
        .rposition(|&lower| clearness >= lower)
        .unwrap_or(0)
}

/// The five luminance-distribution parameters a, b, c, d, e of Perez et al.
/// 1993 for a sun zenith angle (radians), clearness and brightness.
///
/// Eq. 6 is a linear fit in zenith angle and brightness; the overcast bin
/// uses eqs. 7 and 8 for c and d. Within the middle clearness range the
/// brightness is held at or above 0.2 as the paper prescribes.
pub fn perez_parameters(sun_zenith: f64, clearness: f64, brightness: f64, bin: usize) -> [f64; 5] {
    let brightness = if clearness > 1.065 && clearness < 2.8 {
        brightness.max(0.2)
    } else {
        brightness
    };
    let table = &PEREZ_1993_TABLE_1[bin];
    let fit = |parameter: usize| {
        let row = &table[4 * parameter..4 * parameter + 4];
        row[0] + row[1] * sun_zenith + brightness * (row[2] + row[3] * sun_zenith)
    };
    let mut parameters = [fit(0), fit(1), fit(2), fit(3), fit(4)];
    if bin == 0 {
        let c = &table[8..12];
        let d = &table[12..16];
        parameters[2] = (brightness * (c[0] + c[1] * sun_zenith)).powf(c[2]).exp() - c[3];
        parameters[3] = -(brightness * (d[0] + d[1] * sun_zenith)).exp() + d[2] + brightness * d[3];
    }
    parameters
}

/// Perez et al. 1993 eq. 1: luminance relative to an unnormalised zenith for
/// a sky point at `sun_angle` radians from the sun and `zenith_angle`
/// radians from the zenith.
pub fn relative_luminance(parameters: &[f64; 5], sun_angle: f64, zenith_angle: f64) -> f64 {
    let [a, b, c, d, e] = *parameters;
    (1.0 + a * (b / zenith_angle.cos()).exp())
        * (1.0 + c * (d * sun_angle).exp() + e * sun_angle.cos() * sun_angle.cos())
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::sky::{patch_directions, patch_solid_angles};

    fn gothenburg() -> SkySite {
        SkySite {
            latitude_degrees: 57.66,
            longitude_degrees: 12.28,
            time_zone_hours: 1.0,
        }
    }

    #[test]
    fn patch_table_matches_shared_geometry() {
        for basis in [SkyBasis::Tregenza, SkyBasis::ReinhartMf2] {
            let table = PatchTable::new(basis);
            let directions = patch_directions(basis);
            let solid_angles = patch_solid_angles(basis);
            assert_eq!(table.len(), basis.row_count());
            for patch in 0..table.len() {
                let expected = directions[patch];
                let actual = table.direction(patch);
                for (component, value) in [expected.x, expected.y, expected.z].iter().enumerate() {
                    assert!(
                        (actual[component] - *value as f64).abs() < 1e-5,
                        "patch {patch} direction differs: {actual:?} vs {expected:?}"
                    );
                }
                assert!(
                    (table.solid_angle[patch] - solid_angles[patch]).abs() < 1e-5,
                    "patch {patch} solid angle differs"
                );
            }
            let dome: f64 = table
                .solid_angle
                .iter()
                .skip(1)
                .map(|&value| value as f64)
                .sum();
            assert!((dome - 2.0 * std::f64::consts::PI).abs() < 1e-4);
        }
    }

    #[test]
    fn sun_is_south_at_solar_noon_in_the_north() {
        let position = solar_position(&gothenburg(), 172, 12.0 + 0.181, 0.0);
        let direction = position.direction();
        let horizontal = (direction[0] * direction[0] + direction[1] * direction[1]).sqrt();
        assert!(
            direction[1] / horizontal < -0.99,
            "sun should be south: {direction:?}"
        );
        assert!(position.altitude.to_degrees() > 55.0 && position.altitude.to_degrees() < 56.5);
        let midnight = solar_position(&gothenburg(), 172, 0.5, 0.0);
        assert!(!midnight.sun_up());
    }

    #[test]
    fn table_sine_tracks_the_exact_sine_to_the_table_step() {
        for step in 0..2000 {
            let angle = step as f64 * 0.0021 - 2.0;
            let error = (table_sine(angle) - angle.sin()).abs();
            assert!(error < 1.6e-3, "angle {angle}: error {error}");
        }
        assert_eq!(table_sine(std::f64::consts::FRAC_PI_2), 1.0);
        assert_eq!(table_cosine(0.0), 1.0);
    }

    #[test]
    fn clearness_bins_follow_table_bounds() {
        assert_eq!(clearness_bin(1.0), 0);
        assert_eq!(clearness_bin(1.0649), 0);
        assert_eq!(clearness_bin(1.065), 1);
        assert_eq!(clearness_bin(2.8), 5);
        assert_eq!(clearness_bin(11.9), 7);
    }

    #[test]
    fn overcast_sky_is_darkest_at_the_horizon_and_sums_to_diffuse() {
        let site = gothenburg();
        let steps = [SkyStep {
            day_of_year: 172,
            hour: 12.5,
            direct_normal: 0.0,
            diffuse_horizontal: 300.0,
        }];
        let options = AllWeatherSkyOptions::default();
        let result = all_weather_sky_matrix(&site, &steps, &options).unwrap();
        assert_eq!(result.sun_up, vec![true]);
        let matrix = &result.matrix;
        let zenith = matrix.get(145, 0)[1];
        let horizon = matrix.get(1, 0)[1];
        assert!(
            zenith > 2.0 * horizon,
            "overcast zenith {zenith} vs horizon {horizon}"
        );
        let table = PatchTable::new(SkyBasis::Tregenza);
        let horizontal: f64 = (1..146)
            .map(|patch| {
                matrix.get(patch, 0)[1] as f64
                    * (table.altitude[patch] as f64).sin()
                    * table.solid_angle[patch] as f64
            })
            .sum();
        // Diffuse illuminance / 179 / sky_color green: the green channel
        // integrates to the measured diffuse horizontal radiance.
        let expected = 300.0
            * (97.24 - 0.46 * (0.07 * 11.0 - 0.075f64).exp()
                + 12.0 * (90.0f64 - 55.8).to_radians().cos()
                + 0.0)
            / 179.0
            * 1.004;
        // Loose check: the brightness term depends on air mass; only the
        // order of magnitude is pinned here, the oracle test pins the rest.
        assert!(horizontal > 0.5 * expected && horizontal < 1.5 * expected);
        assert!(matrix.get(0, 0)[0] > 0.0);
    }

    #[test]
    fn clear_sky_puts_the_direct_component_in_four_patches() {
        let site = gothenburg();
        let step = SkyStep {
            day_of_year: 172,
            hour: 12.5,
            direct_normal: 800.0,
            diffuse_horizontal: 100.0,
        };
        let options = AllWeatherSkyOptions::default();
        let with_sun = all_weather_sky_matrix(&site, &[step], &options).unwrap();
        let without = all_weather_sky_matrix(
            &site,
            &[SkyStep {
                direct_normal: 0.0,
                ..step
            }],
            &options,
        )
        .unwrap();
        let brighter = (1..146)
            .filter(|&patch| {
                with_sun.matrix.get(patch, 0)[1] > 20.0 * without.matrix.get(patch, 0)[1]
            })
            .count();
        assert!(
            brighter >= 1 && brighter <= 4,
            "{brighter} patches carry the sun"
        );
    }

    #[test]
    fn night_steps_are_black_and_rejections_are_explicit() {
        let site = gothenburg();
        let steps = [SkyStep {
            day_of_year: 1,
            hour: 0.5,
            direct_normal: 0.0,
            diffuse_horizontal: 0.0,
        }];
        let result =
            all_weather_sky_matrix(&site, &steps, &AllWeatherSkyOptions::default()).unwrap();
        assert!(
            result
                .matrix
                .values
                .iter()
                .flatten()
                .all(|&value| value == 0.0)
        );
        assert_eq!(result.sun_up, vec![false]);
        assert!(all_weather_sky_matrix(&site, &[], &AllWeatherSkyOptions::default()).is_err());
        let bad = [SkyStep {
            direct_normal: -1.0,
            ..steps[0]
        }];
        assert!(all_weather_sky_matrix(&site, &bad, &AllWeatherSkyOptions::default()).is_err());
    }
}
