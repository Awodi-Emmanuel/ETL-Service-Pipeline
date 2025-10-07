import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def normalize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Transforms raw record into normalized schema."""
    return {
        "id": record.get("id"),
        "name": (record.get("name") or "").strip(),
        "value": float(record.get("value") or 0),
    }


def transform_dataset(dataset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    logger.info("Transforming dataset")
    return [normalize_record(rec) for rec in dataset]
