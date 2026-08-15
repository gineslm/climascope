from src.aemet import normalize_prec, normalize_daily_row


def test_prec_comma_decimal():
    assert normalize_prec("3,8") == 3.8


def test_prec_explicit_zero():
    assert normalize_prec("0,0") == 0.0


def test_prec_missing_is_none():
    assert normalize_prec(None) is None
    assert normalize_prec("") is None
    assert normalize_prec("nan") is None
    assert normalize_prec("NA") is None
    assert normalize_prec("N/A") is None


def test_prec_normalization_preserves_raw_field():
    row = {"fecha": "2025-01-01", "prec": "3,8"}
    normalized = normalize_daily_row(row)

    assert normalized["prec"] == "3,8"
    assert normalized["prcp"] == 3.8
    assert row["prec"] == "3,8"
