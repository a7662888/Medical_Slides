from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class PreprocessingConfig:
    """Configuration for a conservative clinical research cleaning pass."""

    participant_id_col: str = "participant_id"
    diagnosis_col: str = "diagnosis_group"
    required_columns: tuple[str, ...] = (
        "participant_id",
        "age",
        "sex",
        "diagnosis_group",
    )
    cognitive_score_columns: tuple[str, ...] = ("mmse", "moca", "cdr_global")
    missing_tokens: tuple[str, ...] = ("", "NA", "N/A", "Unknown", "unknown", "None")
    valid_diagnosis_groups: tuple[str, ...] = (
        "Control",
        "SCD",
        "MCI",
        "Dementia",
        "AD-MCI",
        "PD-MCI",
        "MCR",
    )
    categorical_columns: tuple[str, ...] = ("sex", "diagnosis_group")
    numeric_columns: tuple[str, ...] = ("age", "education_years", "mmse", "moca", "cdr_global")
    audit_columns: tuple[str, ...] = field(default_factory=tuple)


def validate_required_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def standardize_missing_values(df: pd.DataFrame, missing_tokens: Iterable[str]) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned = cleaned.replace(list(missing_tokens), pd.NA)
    return cleaned


def normalize_categories(df: pd.DataFrame, categorical_columns: Iterable[str]) -> pd.DataFrame:
    cleaned = df.copy()
    for column in categorical_columns:
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].astype("string").str.strip()
    return cleaned


def coerce_numeric_columns(df: pd.DataFrame, numeric_columns: Iterable[str]) -> pd.DataFrame:
    cleaned = df.copy()
    for column in numeric_columns:
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
    return cleaned


def flag_duplicate_ids(df: pd.DataFrame, participant_id_col: str) -> pd.Series:
    if participant_id_col not in df.columns:
        raise ValueError(f"Missing participant ID column: {participant_id_col}")
    return df.duplicated(subset=[participant_id_col], keep=False)


def validate_diagnosis_groups(df: pd.DataFrame, config: PreprocessingConfig) -> None:
    if config.diagnosis_col not in df.columns:
        return
    observed = set(df[config.diagnosis_col].dropna().astype(str))
    invalid = sorted(observed.difference(config.valid_diagnosis_groups))
    if invalid:
        raise ValueError(f"Invalid diagnosis groups: {', '.join(invalid)}")


def add_quality_flags(df: pd.DataFrame, config: PreprocessingConfig) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned["qc_duplicate_participant_id"] = flag_duplicate_ids(
        cleaned,
        config.participant_id_col,
    )
    available_scores = [col for col in config.cognitive_score_columns if col in cleaned.columns]
    if available_scores:
        cleaned["qc_missing_all_cognitive_scores"] = cleaned[available_scores].isna().all(axis=1)
    return cleaned


def clean_dataset(df: pd.DataFrame, config: PreprocessingConfig | None = None) -> pd.DataFrame:
    """Run a minimal, auditable preprocessing pipeline.

    This function intentionally avoids dropping rows. It standardizes values,
    coerces expected numeric columns, validates group labels, and adds quality
    flags so exclusion decisions remain explicit in downstream notebooks.
    """

    config = config or PreprocessingConfig()
    validate_required_columns(df, config.required_columns)

    cleaned = standardize_missing_values(df, config.missing_tokens)
    cleaned = normalize_categories(cleaned, config.categorical_columns)
    cleaned = coerce_numeric_columns(cleaned, config.numeric_columns)
    validate_diagnosis_groups(cleaned, config)
    cleaned = add_quality_flags(cleaned, config)
    return cleaned
