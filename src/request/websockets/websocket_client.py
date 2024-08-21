import time
import asyncio
import websockets
import json
import os
from src.helpers.logging import Logger
from dotenv import load_dotenv

logger = Logger("WebSocketClient").get_logger()
load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
FINNHUB_SOCKET = os.getenv("FINNHUB_SOCKET")

class FinnhubWebSocketClient:
	def __init__(self, symbol: str, enable_failsafe: bool = True):
		self.symbol = symbol
		self.url = f"{FINNHUB_SOCKET}?token={FINNHUB_API_KEY}"
		self.enable_failsafe = enable_failsafe
		self.api_calls_count = 0
		self.api_calls_reset_time = time.time()
	
	async def rate_limiter(self):
		if self.enable_failsafe:
			current_time = time.time()
			if current_time - self.api_calls_reset_time >= 1:
				self.api_calls_count = 0
				self.api_calls_reset_time = current_time
			
			if self.api_calls_count >= 30:
				logger.warning("Rate limit reached, pausing processing")
				await asyncio.sleep(1)
				self.api_calls_count = 0
				self.api_calls_reset_time = time.time()
			
			self.api_calls_count += 1
	
	async def connect(self):
		async with websockets.connect(self.url) as websocket:
			await self.subscribe(websocket)
			await self.receive(websocket)
	
	async def subscribe(self, websocket):
		subscribe_message = json.dumps({"type": "subscribe", "symbol": self.symbol})
		await websocket.send(subscribe_message)
		logger.info(f"Subscribed to {self.symbol}")
	
	async def receive(self, websocket):
		while True:
			try:
				message = await websocket.recv()
				data = json.loads(message)
				await self.rate_limiter()  # Throttle processing if needed
				logger.info(f"Received data: {data}")
				# Here you would send data to Kafka or process it
			except websockets.ConnectionClosed:
				logger.error("WebSocket connection closed")
				break


if __name__ == "__main__":
	symbol = "AAPL"  # Example stock symbol
	client = FinnhubWebSocketClient(symbol)
	asyncio.run(client.connect())
