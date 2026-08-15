import pandas as pd

from src.water_precip_aggregate import aggregate_precipitation


def test_missing_day_is_not_zero_and_period_is_incomplete():
    df = pd.DataFrame({
        "fecha": pd.to_datetime(["2025-01-01", "2025-01-03"]),
        "prcp": [2.0, 0.0],
    })

    monthly, annual = aggregate_precipitation(df, "2025-01-01", "2025-01-03")

    assert monthly.iloc[0]["expected_days"] == 3
    assert monthly.iloc[0]["observed_prcp_days"] == 2
    assert monthly.iloc[0]["missing_prcp_days"] == 1
    assert monthly.iloc[0]["prcp_total_mm"] is None
    assert monthly.iloc[0]["complete"] is False
    assert annual.iloc[0]["coverage_pct"] == round(2 / 3 * 100, 3)


def test_complete_period_sums_explicit_zero():
    df = pd.DataFrame({
        "fecha": pd.to_datetime(["2025-01-01", "2025-01-02"]),
        "prcp": [2.0, 0.0],
    })

    monthly, annual = aggregate_precipitation(df, "2025-01-01", "2025-01-02")

    assert monthly.iloc[0]["prcp_total_mm"] == 2.0
    assert monthly.iloc[0]["complete"] is True
    assert annual.iloc[0]["prcp_total_mm"] == 2.0
