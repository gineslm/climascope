from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from src.water_precip_qc import load_station_records


def main() -> None:
    parser = argparse.ArgumentParser(description="Detailed W1 AEMET precipitation QC")
    parser.add_argument("--raw-dir", default="data/raw/aemet")
    parser.add_argument("--start", default="2011-01-01")
    parser.add_argument("--end", default="2025-12-31")
    parser.add_argument("--stations", nargs="+", default=["8416", "7012D", "3195"])
    args = parser.parse_args()

    out_dir = Path(args.raw_dir)
    summary = []
    missing_rows = []

    for station in args.stations:
        df = load_station_records(out_dir, station, args.start, args.end)
        expected = pd.date_range(args.start, args.end, freq="D")
        observed = pd.DatetimeIndex(df["fecha"]).normalize().drop_duplicates() if not df.empty else pd.DatetimeIndex([])
        missing_dates = expected.difference(observed)

        raw_missing = df[df["prec"].isna() | (df["prec"].astype(str).str.strip() == "")].copy()
        raw_missing["station_id"] = station
        if not raw_missing.empty:
            missing_rows.append(raw_missing[["station_id", "fecha", "prec"]])

        annual = (
            df.assign(year=df["fecha"].dt.year)
            .groupby("year")
            .agg(observed_days=("fecha", "nunique"), prec_missing=("prcp", lambda s: int(s.isna().sum())))
            .reset_index()
        )
        annual["station_id"] = station
        annual["expected_days"] = annual["year"].map(lambda y: len(pd.date_range(f"{y}-01-01", f"{y}-12-31", freq="D")))
        annual["coverage_pct"] = (annual["observed_days"] / annual["expected_days"] * 100).round(3)
        annual.to_csv(out_dir / f"{station}_precipitation_qc_annual.csv", index=False)

        summary.append({
            "station_id": station,
            "missing_dates": [d.date().isoformat() for d in missing_dates],
            "missing_date_count": len(missing_dates),
            "raw_prec_missing_count": int(len(raw_missing)),
            "first_data": observed.min().date().isoformat() if len(observed) else "",
            "last_data": observed.max().date().isoformat() if len(observed) else "",
        })

    (out_dir / "precipitation_qc_detail.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    if missing_rows:
        pd.concat(missing_rows, ignore_index=True).to_csv(out_dir / "precipitation_missing_values.csv", index=False)
    else:
        pd.DataFrame(columns=["station_id", "fecha", "prec"]).to_csv(out_dir / "precipitation_missing_values.csv", index=False)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"Annual QC written under {out_dir}")


if __name__ == "__main__":
    main()
