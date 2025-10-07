import logging

from .extractor import extract_from_sources
from .loader import SQLiteLoader
from .transformer import transform_dataset

logger = logging.getLogger(__name__)


async def run_etl_pipeline(urls: list[str], db_path: str = "etl_service.db"):
    logger.info("Running ETL-Service-Pipeline")
    raw_data = await extract_from_sources(urls)
    flattened = [item for batch in raw_data for item in (batch or [])]
    transformed = transform_dataset(flattened)

    loader = SQLiteLoader(db_path)
    loader.initialize_database()
    loader.load_records(transformed)
    logger.info(
        f"ETL pipeline completed successfully. {len(transformed)} items processed."
    )
