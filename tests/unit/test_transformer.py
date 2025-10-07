from etl_service_pipeline.transformer import normalize_record, transform_dataset


def test_normalize_record_trims_name_and_converts_value():
    record = {"id": "123", "name": " Alice ", "value": "45.6"}
    normalized = normalize_record(record)
    assert normalized["id"] == "123"
    assert normalized["name"] == "Alice"
    assert isinstance(normalized["value"], float)
    assert normalized["value"] == 45.6


def test_normalize_record_handles_missing_fields():
    record = {"id": "001"}
    normalized = normalize_record(record)
    assert normalized["name"] == ""
    assert normalized["value"] == 0.0


def test_transform_dataset_applies_normalization():
    records = [
        {"id": "1", "name": " John ", "value": "5"},
        {"id": "2", "name": "  Doe", "value": "10"},
    ]
    result = transform_dataset(records)
    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[1]["value"] == 10.0
