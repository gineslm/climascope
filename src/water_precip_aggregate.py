from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.water_precip_qc import load_station_records


def _complete_daily_frame(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    dates = pd.date_range(start, end, freq="D")
    base = pd.DataFrame({"fecha": dates})
    if df.empty:
        base["prcp"] = pd.NA
        return base
    values = df[["fecha", "prcp"]].copy()
    values["fecha"] = pd.to_datetime(values["fecha"]).dt.normalize()
    return base.merge(values, on="fecha", how="left")


def aggregate_precipitation(df: pd.DataFrame, start: str, end: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Aggregate daily precipitation while preserving coverage quality metadata.

    Missing dates and missing precipitation values are never converted to zero.
    ``prcp_observed_total_mm`` is the sum of available precipitation values only;
    ``complete`` identifies periods with observations for every expected day.
    Consumers must use the coverage fields to decide whether a total is fit for
    a particular analysis.
    """
    daily = _complete_daily_frame(df, start, end)
    daily["period_month"] = daily["fecha"].dt.to_period("M").astype(str)
    daily["period_year"] = daily["fecha"].dt.year

    def agg(group: pd.DataFrame, key: str) -> dict:
        expected = len(group)
        observed = int(group["prcp"].notna().sum())
        missing = expected - observed
        total = group["prcp"].sum(min_count=1)
        return {
            key: group[key].iloc[0],
            "expected_days": expected,
            "observed_prcp_days": observed,
            "missing_prcp_days": missing,
            "coverage_pct": round(observed / expected * 100, 3) if expected else 0.0,
            "prcp_observed_total_mm": float(total) if pd.notna(total) else None,
            "complete": missing == 0,
        }

    monthly = pd.DataFrame([agg(g, "period_month") for _, g in daily.groupby("period_month", sort=True)])
    annual = pd.DataFrame([agg(g, "period_year") for _, g in daily.groupby("period_year", sort=True)])
    return monthly, annual


def aggregate_station(raw_dir: str | Path, station_id: str, start: str, end: str, out_dir: str | Path | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = load_station_records(raw_dir, station_id, start, end)
    monthly, annual = aggregate_precipitation(df, start, end)
    if out_dir is not None:
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        monthly.to_csv(out / f"{station_id}_precip_monthly.csv", index=False)
        annual.to_csv(out / f"{station_id}_precip_annual.csv", index=False)
    return monthly, annual
