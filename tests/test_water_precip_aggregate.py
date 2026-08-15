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
    assert monthly.iloc[0]["prcp_observed_total_mm"] == 2.0
    assert not monthly.iloc[0]["complete"]
    assert annual.iloc[0]["coverage_pct"] == round(2 / 3 * 100, 3)
    assert annual.iloc[0]["prcp_observed_total_mm"] == 2.0


def test_complete_period_sums_explicit_zero():
    df = pd.DataFrame({
        "fecha": pd.to_datetime(["2025-01-01", "2025-01-02"]),
        "prcp": [2.0, 0.0],
    })

    monthly, annual = aggregate_precipitation(df, "2025-01-01", "2025-01-02")

    assert monthly.iloc[0]["prcp_observed_total_mm"] == 2.0
    assert bool(monthly.iloc[0]["complete"])
    assert annual.iloc[0]["prcp_observed_total_mm"] == 2.0


def test_missing_precipitation_is_not_treated_as_zero():
    df = pd.DataFrame({
        "fecha": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]),
        "prcp": [2.0, pd.NA, 0.0],
    })

    monthly, _ = aggregate_precipitation(df, "2025-01-01", "2025-01-03")

    assert monthly.iloc[0]["observed_prcp_days"] == 2
    assert monthly.iloc[0]["missing_prcp_days"] == 1
    assert monthly.iloc[0]["prcp_observed_total_mm"] == 2.0
    assert not monthly.iloc[0]["complete"]
