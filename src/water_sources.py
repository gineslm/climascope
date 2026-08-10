from pathlib import Path

import pandas as pd
import yaml

REQUIRED_FIELDS = (
    "id",
    "provider",
    "dataset",
    "category",
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
)


def load_source_registry(path):
    path = Path(path)
    config = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    sources = config.get("sources")
    if not isinstance(sources, list):
        raise ValueError(f"El registro debe contener una lista 'sources': {path}")

    ids = [source.get("id") for source in sources]
    if any(not source_id for source_id in ids):
        raise ValueError("Todas las fuentes deben tener un id")
    if len(ids) != len(set(ids)):
        raise ValueError("Los source_id deben ser únicos")

    missing = {
        source["id"]: [field for field in REQUIRED_FIELDS if field not in source]
        for source in sources
    }
    missing = {source_id: fields for source_id, fields in missing.items() if fields}
    if missing:
        raise ValueError(f"Campos ausentes en el registro: {missing}")

    return sources


def source_registry_dataframe(sources):
    """Representa el registro sin transformar ni derivar indicadores."""
    return pd.DataFrame(sources, columns=REQUIRED_FIELDS)


def audit_registry(sources):
    """Hace QC estructural del registro; no valida los datasets externos."""
    rows = []
    for source in sources:
        url = source.get("url_or_endpoint")
        rows.append(
            {
                "source_id": source["id"],
                "provider": source["provider"],
                "dataset": source["dataset"],
                "variable": source["variable"],
                "url_or_endpoint": url or "",
                "access_method": source["access_method"],
                "format": source["format"],
                "geographic_coverage": source["geographic_coverage"],
                "spatial_resolution": source["spatial_resolution"],
                "temporal_coverage": source["temporal_coverage"],
                "temporal_resolution": source["temporal_resolution"],
                "unit": source["unit"],
                "retrieval_status": source["retrieval_status"],
                "validation_status": source["validation_status"],
                "limitations": source["limitations"],
                "notes": source["notes"],
            }
        )
    return pd.DataFrame(rows)
