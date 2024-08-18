import pytest
import httpx
from src.helpers.logging import Logger
from src.request.httpx.httpx_request import HTTPXRequest

logger = Logger("HTTPXRequestTest").get_logger()

@pytest.mark.asyncio
async def test_httpx_request_dict_success():
    request_url = "https://jsonplaceholder.typicode.com/todos/1"
    mock_response_data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }

    httpx_request = HTTPXRequest()
    result = await httpx_request.httpx_request_dict(request_url)

    assert result == mock_response_data
    logger.info(f"Test success: {result}")
