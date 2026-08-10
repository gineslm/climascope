import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from water_qc import write_water_results
from water_sources import audit_registry, load_source_registry, source_registry_dataframe


def main():
    config_path = ROOT / "config/water_sources.yml"
    output_dir = ROOT / "results/water"

    sources = load_source_registry(config_path)
    audit_df = audit_registry(sources)
    registry_df = source_registry_dataframe(sources)

    output_dir.mkdir(parents=True, exist_ok=True)
    registry_df.to_csv(output_dir / "source_registry.csv", index=False)
    write_water_results(audit_df, output_dir)

    print(f"OK: {output_dir / 'source_registry.csv'}")
    print(f"OK: {output_dir / 'source_audit.csv'}")


if __name__ == "__main__":
    main()
