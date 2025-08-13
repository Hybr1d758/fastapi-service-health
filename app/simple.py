from fastapi import FastAPI, Request


app = FastAPI(title="network-test")


@app.get("/")
async def root():
	return {"ok": True}


@app.get("/ping")
async def ping():
	return {"pong": True}


@app.get("/ip")
async def ip(request: Request):
	return {"ip": request.client.host}


@app.get("/headers")
async def headers(request: Request):
	return {"headers": dict(request.headers)}


