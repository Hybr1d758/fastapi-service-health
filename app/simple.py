from fastapi import FastAPI, Request
from datetime import datetime, timezone


app = FastAPI(title="network-test")


@app.get("/")
async def root():
	return {"ok": True}


@app.get("/ping")
async def ping():n
	return {"pong": True}


@app.get("/ip")
async def ip(request: Request):
	return {"ip": request.client.host}


@app.get("/headers")
async def headers(request: Request):
	return {"headers": dict(request.headers)}


@app.get("/time")
async def time_utc():
	now = datetime.now(timezone.utc)
	return {"iso_utc": now.isoformat(), "epoch_ms": int(now.timestamp() * 1000)}


