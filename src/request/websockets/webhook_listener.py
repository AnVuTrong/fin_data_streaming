import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Header, HTTPException

load_dotenv()
app = FastAPI()

FINNHUB_SECRET_KEY = os.getenv("FINNHUB_SECRET_KEY")


@app.post("/webhook")
async def webhook(
		request: Request,
		x_finnhub_secret: str = Header(None)
):
	if x_finnhub_secret != FINNHUB_SECRET_KEY:
		raise HTTPException(status_code=403, detail="Unauthorized")
	
	payload = await request.json()
	# Log or process the data here
	print(f"Received data: {payload}")
	
	return {"status": "success"}


if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=5000)
