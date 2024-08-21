run:
	PYTHONPATH=. poetry run python src/main.py
test:
	pytest
test_websocket_client:
	PYTHONPATH=. poetry run python src/request/websockets/websocket_client.py
test_websocket_listener:
	PYTHONPATH=. poetry run python src/request/websockets/webhook_listener.py
run_webhook_listener:
	PYTHONPATH=. poetry run uvicorn src.request.websockets.webhook_listener:app --host 0.0.0.0 --port 5000
