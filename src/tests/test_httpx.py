import pytest
import httpx
from src.helpers.logging import Logger
from src.request.httpx.httpx_request import HTTPXRequest

logger = Logger("HTTPXRequestTest", directory="testing_logs").get_logger()

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


@pytest.mark.asyncio
async def test_httpx_request_dict_failure(mocker):
	request_url = "https://jsonplaceholder.typicode.com/todos/1"
	
	# Create a mock response with a 404 status code
	mock_response = httpx.Response(
		status_code=404,  # Not Found
		request=httpx.Request("GET", request_url)
	)
	
	# Mock the httpx.AsyncClient.get method to return the mock response
	mocker.patch(
		"httpx.AsyncClient.get",
		return_value=mock_response
	)
	
	httpx_request = HTTPXRequest()
	result = await httpx_request.httpx_request_dict(request_url)
	
	# Expecting an empty dictionary since the request failed
	assert result == {}
	logger.info(f"Test failure: {result}")
    