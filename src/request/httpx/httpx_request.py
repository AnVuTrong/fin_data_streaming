import asyncio
import os
import httpx
import dotenv
from src.helpers.logging import Logger

logger = Logger("HTTPXRequest").get_logger()


class HTTPXRequest:
	def __init__(self, attempts: int = 3, timeout: float = 20.0):
		self.timeout = timeout
		self.attempts = attempts
	
	async def httpx_request_dict(self, request_url: str) -> dict:
		for attempt in range(self.attempts):  # 3 attempts default
			try:
				async with httpx.AsyncClient(timeout=self.timeout) as client:
					response = await client.get(request_url)
					response.raise_for_status()
					response_dict = response.json()
					return response_dict
			except (httpx.ConnectError, ValueError, KeyError, httpx.HTTPStatusError, httpx.TimeoutException) as e:
				logger.error(f"Error occurred: {e}")
				if attempt < 2:
					await asyncio.sleep(1)
				else:
					return {}, {}
