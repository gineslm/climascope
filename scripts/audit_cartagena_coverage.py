from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.water_precip_qc import load_station_records

RAW_DIR = Path("data/raw/aemet")
STATION = "7012D"
START = "2016-02-22"
END = "2025-12-31"


def main() -> None:
    df = load_station_records(RAW_DIR, STATION, START, END)
    expected = pd.date_range(START, END, freq="D")
    observed = pd.DatetimeIndex(df["fecha"]).normalize().drop_duplicates()

    rows = []
    for year in range(2016, 2026):
        y_start = max(pd.Timestamp(f"{year}-01-01"), pd.Timestamp(START))
        y_end = min(pd.Timestamp(f"{year}-12-31"), pd.Timestamp(END))
        if y_start > y_end:
            continue
        exp = pd.date_range(y_start, y_end, freq="D")
        obs = observed[(observed >= y_start) & (observed <= y_end)]
        missing = exp.difference(obs)
        rows.append({
            "station_id": STATION,
            "year": year,
            "expected_days": len(exp),
            "observed_days": len(obs),
            "missing_days": len(missing),
            "coverage_pct": round(len(obs) / len(exp) * 100, 3),
            "first_observed": obs.min().date().isoformat() if len(obs) else "",
            "last_observed": obs.max().date().isoformat() if len(obs) else "",
        })

    annual = pd.DataFrame(rows)
    annual.to_csv(RAW_DIR / "7012D_precipitation_qc_annual_window_2016_2025.csv", index=False)

    result = {
        "station_id": STATION,
        "window_start": START,
        "window_end": END,
        "expected_days": len(expected),
        "observed_days": len(observed),
        "missing_days": len(expected.difference(observed)),
        "coverage_pct": round(len(observed) / len(expected) * 100, 3),
        "annual": rows,
    }
    (RAW_DIR / "7012D_precipitation_qc_window_2016_2025.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(annual.to_string(index=False))
    print("\nWindow summary:")
    print(json.dumps({k: v for k, v in result.items() if k != "annual"}, indent=2))


if __name__ == "__main__":
    main()
