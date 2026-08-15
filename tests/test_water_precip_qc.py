import pandas as pd

from src.water_precip_qc import audit_precipitation


def test_qc_counts_zeros_positive_and_missing():
    df = pd.DataFrame(
        {
            "fecha": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-04"]),
            "prcp": [0.0, 3.8, None],
        }
    )

    result = audit_precipitation(df, "2025-01-01", "2025-01-04")

    assert result["target_days"] == 4
    assert result["observed_days"] == 3
    assert result["missing_days"] == 1
    assert result["coverage_pct"] == 75.0
    assert result["prec_zero_days"] == 1
    assert result["prec_positive_days"] == 1
    assert result["prec_missing_days"] == 1
    assert result["missing_dates"] == ["2025-01-03"]


def test_qc_full_coverage_has_no_missing_dates():
    df = pd.DataFrame(
        {
            "fecha": pd.to_datetime(["2025-01-01", "2025-01-02"]),
            "prcp": [0.0, 1.2],
        }
    )

    result = audit_precipitation(df, "2025-01-01", "2025-01-02")

    assert result["coverage_pct"] == 100.0
    assert result["missing_dates"] == []
