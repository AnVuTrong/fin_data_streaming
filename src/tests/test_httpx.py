# import pytest
# import httpx
# from src.helpers.logging import Logger
# from src.request.httpx.httpx_request import HTTPXRequest
#
# logger = Logger("HTTPXRequestTest").get_logger()
#
# @pytest.mark.asyncio
# async def test_httpx_request_dict_success(mocker):
#     request_url = "https://jsonplaceholder.typicode.com/todos/1"
#     mock_response = {
#         "userId": 1,
#         "id": 1,
#         "title": "delectus aut autem",
#         "completed": False
#     }
#
#     # Mock the httpx.AsyncClient.get method to return a mock response
#     mocker.patch(
# 	    "httpx.AsyncClient.get",
# 	    return_value=httpx.Response(200, json=mock_response)
#     )
#
#     httpx_request = HTTPXRequest()
#     result = await httpx_request.httpx_request_dict(request_url)
#
#     assert result == mock_response
#     logger.info(f"Test success: {result}")
#
# @pytest.mark.asyncio
# async def test_httpx_request_dict_failure(mocker):
#     request_url = "https://jsonplaceholder.typicode.com/invalid_url"
#
#     # Mock the httpx.AsyncClient.get method to raise an HTTPStatusError
#     mocker.patch(
# 	    "httpx.AsyncClient.get",
# 	    side_effect=httpx.HTTPStatusError(
# 		    "Not Found",
# 		    request=None,
# 		    response=httpx.Response(404)
# 	    )
#     )
#
#     httpx_request = HTTPXRequest()
#     result = await httpx_request.httpx_request_dict(request_url)
#
#     assert result == {}
#     logger.info(f"Test failure: {result}")
