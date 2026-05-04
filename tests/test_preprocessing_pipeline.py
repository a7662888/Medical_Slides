import pandas as pd
import pytest

from dementia_ai_research.preprocessing import PreprocessingConfig, clean_dataset


def test_clean_dataset_flags_duplicate_ids_and_missing_scores():
    df = pd.DataFrame(
        {
            "participant_id": ["A001", "A001", "A002"],
            "age": ["72", "72", "68"],
            "sex": ["Female", "Female", "Male"],
            "diagnosis_group": ["MCI", "MCI", "Control"],
            "mmse": ["NA", "NA", "28"],
            "moca": ["", "", "26"],
        }
    )

    cleaned = clean_dataset(df)

    assert cleaned["age"].tolist() == [72, 72, 68]
    assert cleaned["qc_duplicate_participant_id"].tolist() == [True, True, False]
    assert cleaned["qc_missing_all_cognitive_scores"].tolist() == [True, True, False]


def test_clean_dataset_rejects_unknown_group():
    df = pd.DataFrame(
        {
            "participant_id": ["A001"],
            "age": [72],
            "sex": ["Female"],
            "diagnosis_group": ["Unclear"],
        }
    )

    with pytest.raises(ValueError, match="Invalid diagnosis groups"):
        clean_dataset(df, PreprocessingConfig())
