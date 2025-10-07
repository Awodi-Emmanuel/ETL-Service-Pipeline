from unittest.mock import AsyncMock, MagicMock

import pytest

from etl_service_pipeline.extractor import Extractor


@pytest.mark.asyncio
async def test_fetch_json_returns_data():
    """Test that fetch_json returns parsed JSON from a mocked HTTP request."""

    # ---- mock response object returned from async with ----
    mock_response = MagicMock()
    mock_response.json = AsyncMock(return_value={"key": "value"})

    # ---- mock async context manager for session.get ----
    mock_context = MagicMock()
    mock_context.__aenter__ = AsyncMock(return_value=mock_response)
    mock_context.__aexit__ = AsyncMock(return_value=None)

    # ---- mock session to return that context manager ----
    mock_session = MagicMock()
    mock_session.get = MagicMock(return_value=mock_context)

    # ---- run the actual method ----
    extractor = Extractor(session=mock_session)
    result = await extractor.fetch_json("https://fake.url")

    # ---- assert ----
    assert result == {"key": "value"}
    mock_session.get.assert_called_once_with("https://fake.url")
    mock_response.json.assert_awaited_once()
