import asyncio
import logging
from typing import Any, Dict, List

import aiohttp

logger = logging.getLogger(__name__)


class Extractor:
    """Handles asynchronous data extraction from multiple URLs."""

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def fetch_json(self, url: str) -> Dict[str, Any]:
        logger.info(f"Extracting data from {url}")
        async with self.session.get(url) as response:
            response.raise_for_status()
            return await response.json()


async def extract_from_sources(urls: List[str]) -> List[Dict[str, Any]]:
    """Extracts JSON data concurrently from a list of URLs."""
    async with aiohttp.ClientSession() as session:
        extractor = Extractor(session)
        tasks = [extractor.fetch_json(url) for url in urls]
        return await asyncio.gather(*tasks)
