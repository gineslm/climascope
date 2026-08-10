import json
from pathlib import Path
import numpy as np
import pandas as pd


def load_aemet_json(path):
    df = pd.DataFrame(json.loads(Path(path).read_text(encoding="utf-8")))
    if df.empty:
        raise ValueError(f"Sin registros: {path}")

    for c in ["tmed", "tmin", "tmax", "prcp"]:
        if c in df:
            df[c] = pd.to_numeric(
                df[c].astype(str)
                .str.replace(",", ".", regex=False)
                .str.replace("Ip", "0", regex=False),
                errors="coerce",
            )

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    return (
        df.dropna(subset=["fecha"])
        .sort_values("fecha")
        .drop_duplicates("fecha")
    )


def _trend_slope(series):
    """Pendiente lineal por año. NaN si no hay suficientes observaciones."""
    s = series.dropna()
    if len(s) < 3 or s.index.nunique() < 3:
        return np.nan
    x = s.index.to_numpy(dtype=float)
    y = s.to_numpy(dtype=float)
    return float(np.polyfit(x, y, 1)[0])


def calculate(df, station_id, station_name, thresholds):
    d = df.copy()
    d["year"] = d["fecha"].dt.year
    d["month"] = d["fecha"].dt.month

    for c in ["tmax", "tmin", "prcp"]:
        if c not in d:
            d[c] = np.nan
        d[c] = pd.to_numeric(d[c], errors="coerce")

    hot = thresholds["hot_day_c"]
    extreme = thresholds["extreme_heat_c"]
    warm_night = thresholds["warm_night_c"]
    very_warm = thresholds["very_warm_night_c"]
    warm_months = thresholds["warm_months"]

    d["is_hot_day"] = d["tmax"] > hot
    d["is_extreme_heat"] = d["tmax"] > extreme
    d["is_warm_night"] = d["tmin"] > warm_night
    d["is_very_warm_night"] = d["tmin"] > very_warm

    warm = d[d["month"].isin(warm_months)].copy()

    annual = d.groupby("year").agg(
        tmax_mean=("tmax", "mean"),
        tmin_mean=("tmin", "mean"),
        tmed_mean=("tmed", "mean"),
        precipitation_mm=("prcp", "sum"),
        hot_days=("is_hot_day", "sum"),
        extreme_heat_days=("is_extreme_heat", "sum"),
        warm_nights=("is_warm_night", "sum"),
        very_warm_nights=("is_very_warm_night", "sum"),
        valid_tmax_days=("tmax", "count"),
        valid_tmin_days=("tmin", "count"),
        valid_prcp_days=("prcp", "count"),
    ).reset_index()

    warm_annual = warm.groupby("year").agg(
        warm_tmax_mean=("tmax", "mean"),
        warm_tmin_mean=("tmin", "mean"),
        warm_tmed_mean=("tmed", "mean"),
        warm_precipitation_mm=("prcp", "sum"),
        warm_hot_days=("is_hot_day", "sum"),
        warm_extreme_heat_days=("is_extreme_heat", "sum"),
        warm_season_nights=("is_warm_night", "sum"),
        warm_season_very_warm_nights=("is_very_warm_night", "sum"),
    ).reset_index()

    annual = annual.merge(warm_annual, on="year", how="left")
    annual.insert(0, "station_id", station_id)
    annual.insert(1, "station_name", station_name)

    # Completeness and gaps.
    expected = pd.date_range(d["fecha"].min(), d["fecha"].max(), freq="D")
    observed = pd.DatetimeIndex(d["fecha"].drop_duplicates())
    missing_dates = expected.difference(observed)

    quality = {
        "station_id": station_id,
        "station_name": station_name,
        "start": str(d["fecha"].min().date()),
        "end": str(d["fecha"].max().date()),
        "records": int(len(d)),
        "expected_records": int(len(expected)),
        "missing_calendar_days": int(len(missing_dates)),
        "missing_tmax": int(d["tmax"].isna().sum()),
        "missing_tmin": int(d["tmin"].isna().sum()),
        "missing_tmed": int(d["tmed"].isna().sum()),
        "missing_prcp": int(d["prcp"].isna().sum()),
        "years": int(d["year"].nunique()),
        "thermal_coverage_pct": round(
            100 * (1 - d[["tmax", "tmin"]].isna().any(axis=1).sum() / len(d)), 2
        ),
        "precipitation_coverage_pct": round(
            100 * d["prcp"].notna().mean(), 2
        ),
    }

    # Trend summary. Units are per year.
    trend = {
        "station_id": station_id,
        "station_name": station_name,
        "tmax_mean_trend_c_per_year": _trend_slope(
            annual.set_index("year")["tmax_mean"]
        ),
        "tmin_mean_trend_c_per_year": _trend_slope(
            annual.set_index("year")["tmin_mean"]
        ),
        "hot_days_trend_per_year": _trend_slope(
            annual.set_index("year")["hot_days"]
        ),
        "extreme_heat_days_trend_per_year": _trend_slope(
            annual.set_index("year")["extreme_heat_days"]
        ),
        "warm_nights_trend_per_year": _trend_slope(
            annual.set_index("year")["warm_nights"]
        ),
        "very_warm_nights_trend_per_year": _trend_slope(
            annual.set_index("year")["very_warm_nights"]
        ),
    }

    return annual, quality, trend
