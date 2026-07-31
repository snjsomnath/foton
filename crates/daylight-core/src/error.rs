use std::fmt::{Display, Formatter};

#[derive(Debug, Clone, PartialEq)]
pub enum DaylightError {
    Cancelled,
    InvalidShape { field: &'static str, detail: String },
    InvalidValue { field: &'static str, detail: String },
    Unsupported { detail: String },
    Backend { detail: String },
}

impl Display for DaylightError {
    fn fmt(&self, formatter: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Cancelled => write!(formatter, "analysis was cancelled"),
            Self::InvalidShape { field, detail } => {
                write!(formatter, "invalid shape for {field}: {detail}")
            }
            Self::InvalidValue { field, detail } => {
                write!(formatter, "invalid value for {field}: {detail}")
            }
            Self::Unsupported { detail } => write!(formatter, "unsupported: {detail}"),
            Self::Backend { detail } => write!(formatter, "backend error: {detail}"),
        }
    }
}

impl std::error::Error for DaylightError {}

pub type Result<T> = std::result::Result<T, DaylightError>;
