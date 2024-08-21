run:
	PYTHONPATH=. poetry run python src/main.py
test:
	pytest
test_websocket:
	PYTHONPATH=. poetry run python src/request/websockets/websocket_client.py
