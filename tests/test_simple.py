from fastapi.testclient import TestClient
from app.simple import app


client = TestClient(app)


def test_root():
	r = client.get("/")
	assert r.status_code == 200
	assert r.json() == {"ok": True}


def test_ping():
	r = client.get("/ping")
	assert r.status_code == 200
	assert r.json() == {"pong": True}


def test_ip_and_headers():
	r = client.get("/ip")
	assert r.status_code == 200
	assert "ip" in r.json()

	r = client.get("/headers")
	assert r.status_code == 200
	assert "headers" in r.json()


def test_time():
	r = client.get("/time")
	assert r.status_code == 200
	body = r.json()
	assert "iso_utc" in body and "epoch_ms" in body


