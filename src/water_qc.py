from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "source_id",
    "provider",
    "dataset",
    "variable",
    "url_or_endpoint",
    "access_method",
    "format",
    "geographic_coverage",
    "spatial_resolution",
    "temporal_coverage",
    "temporal_resolution",
    "unit",
    "retrieval_status",
    "validation_status",
    "limitations",
    "notes",
}


def validate_audit_dataframe(df):
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas de auditoría: {sorted(missing)}")

    if df["source_id"].duplicated().any():
        raise ValueError("source_id duplicado en source_audit")

    if df["retrieval_status"].isna().any():
        raise ValueError("retrieval_status no puede ser NULL")

    if df["validation_status"].isna().any():
        raise ValueError("validation_status no puede ser NULL")

    return True


def write_water_results(audit_df, output_dir):
    """Escribe únicamente resultados de auditoría; no calcula scoring."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    validate_audit_dataframe(audit_df)
    path = output_dir / "source_audit.csv"
    audit_df.to_csv(path, index=False)
    return path
