from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from src.aemet import normalize_prec


def _date_range(start: str, end: str) -> pd.DatetimeIndex:
    return pd.date_range(start=start, end=end, freq="D")


def load_station_records(raw_dir: str | Path, station_id: str, start: str, end: str) -> pd.DataFrame:
    """Load raw AEMET JSON chunks for one station and deduplicate by date."""
    raw_dir = Path(raw_dir)
    rows = []
    for path in sorted(raw_dir.glob(f"{station_id}_*.json")):
        if path.name == f"{station_id}_{start}_{end}.json":
            pass
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, list):
            rows.extend(payload)

    if not rows:
        return pd.DataFrame(columns=["fecha", "prec", "prcp"])

    df = pd.DataFrame(rows)
    if "fecha" not in df.columns:
        raise ValueError(f"No existe columna fecha para {station_id}")

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = df.dropna(subset=["fecha"])
    df = df[(df["fecha"] >= pd.Timestamp(start)) & (df["fecha"] <= pd.Timestamp(end))]
    df = df.sort_values("fecha").drop_duplicates(subset=["fecha"], keep="last")
    if "prec" not in df.columns:
        df["prec"] = None
    df["prcp"] = df["prec"].map(normalize_prec)
    return df.reset_index(drop=True)


def audit_precipitation(df: pd.DataFrame, start: str, end: str) -> dict:
    """Return reproducible daily coverage and precipitation QC metrics."""
    expected = _date_range(start, end)
    observed = pd.DatetimeIndex(df["fecha"]) if not df.empty else pd.DatetimeIndex([])
    observed = observed.normalize().drop_duplicates()
    missing_dates = expected.difference(observed)

    prcp = pd.to_numeric(df.get("prcp", pd.Series(dtype=float)), errors="coerce")
    return {
        "target_start": start,
        "target_end": end,
        "target_days": len(expected),
        "observed_days": len(observed),
        "missing_days": len(missing_dates),
        "coverage_pct": round(len(observed) / len(expected) * 100, 3) if len(expected) else 0.0,
        "prec_zero_days": int((prcp == 0).sum()),
        "prec_positive_days": int((prcp > 0).sum()),
        "prec_missing_days": int(prcp.isna().sum()),
        "first_data": observed.min().date().isoformat() if len(observed) else "",
        "last_data": observed.max().date().isoformat() if len(observed) else "",
        "missing_dates": [d.date().isoformat() for d in missing_dates],
    }


def audit_station(raw_dir: str | Path, station_id: str, start: str, end: str) -> dict:
    df = load_station_records(raw_dir, station_id, start, end)
    result = audit_precipitation(df, start, end)
    result["station_id"] = station_id
    return result


def audit_stations(raw_dir: str | Path, stations: list[str], start: str, end: str) -> pd.DataFrame:
    return pd.DataFrame([audit_station(raw_dir, station_id, start, end) for station_id in stations])
