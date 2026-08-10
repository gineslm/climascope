from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from water_qc import validate_audit_dataframe
from water_sources import audit_registry, load_source_registry


CONFIG = ROOT / "config/water_sources.yml"


def test_water_source_registry_loads():
    sources = load_source_registry(CONFIG)
    assert len(sources) >= 8
    assert {source["id"] for source in sources} >= {
        "aemet_precipitation",
        "snczi_flood",
        "water_bodies_surface",
        "water_bodies_groundwater",
        "drought",
        "reservoirs",
        "supply_systems",
    }


def test_water_audit_has_required_structure():
    sources = load_source_registry(CONFIG)
    audit = audit_registry(sources)
    assert not audit.empty
    assert audit["source_id"].is_unique
    assert validate_audit_dataframe(audit) is True


def test_missing_url_is_not_silently_filled():
    sources = load_source_registry(CONFIG)
    supply = next(source for source in sources if source["id"] == "supply_systems")
    assert supply["url_or_endpoint"] is None
    audit = audit_registry([supply])
    assert audit.loc[0, "url_or_endpoint"] == ""
    assert audit.loc[0, "retrieval_status"] == "not_yet_automated"


def test_qc_rejects_duplicate_source_ids():
    sources = load_source_registry(CONFIG)
    audit = audit_registry(sources[:1])
    duplicate = pd.concat([audit, audit], ignore_index=True)
    with pytest.raises(ValueError, match="source_id duplicado"):
        validate_audit_dataframe(duplicate)
