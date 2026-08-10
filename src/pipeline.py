import sys
import yaml
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from aemet import get_daily_data
from indicators import load_aemet_json, calculate


def main():
    load_dotenv(ROOT / ".env")

    cfg = yaml.safe_load((ROOT / "config/stations.yml").read_text())
    thresholds = yaml.safe_load(
        (ROOT / "config/thresholds.yml").read_text()
    )["thresholds"]

    (ROOT / "results").mkdir(parents=True, exist_ok=True)

    annual_rows = []
    quality_rows = []
    trend_rows = []

    for s in cfg["stations"]:
        p = get_daily_data(
            s["id"],
            cfg["period"]["start"],
            cfg["period"]["end"],
            ROOT / "data/raw/aemet",
        )

        df = load_aemet_json(p)
        annual, quality, trend = calculate(
            df, s["id"], s["name"], thresholds
        )

        annual_rows.append(annual)
        quality_rows.append(quality)
        trend_rows.append(trend)

    pd.concat(annual_rows, ignore_index=True).to_csv(
        ROOT / "results/benchmark_annual.csv", index=False
    )

    pd.DataFrame(quality_rows).to_csv(
        ROOT / "results/data_quality.csv", index=False
    )

    pd.DataFrame(trend_rows).to_csv(
        ROOT / "results/climate_trends.csv", index=False
    )

    print("OK: results/benchmark_annual.csv")
    print("OK: results/data_quality.csv")
    print("OK: results/climate_trends.csv")


if __name__ == "__main__":
    main()
