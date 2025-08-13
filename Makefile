.PHONY: run test build docker-run

run:
	uvicorn app.simple:app --host 0.0.0.0 --port 8000 --reload --no-access-log

test:
	pytest -q

build:
	docker build -t fastapi-network-test .

docker-run:
	docker run --rm -p 8000:8000 fastapi-network-test


