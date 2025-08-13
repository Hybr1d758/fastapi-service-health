
## FastAPI Network Test Service

A minimal FastAPI service to quickly test networking, routing, and headers in local or cloud environments.

### Why this is useful (hiring signal)
- Demonstrates you can spin up a clean HTTP service quickly.
- Provides simple, reliable endpoints SREs/DevOps can probe.
- Clear structure, clear instructions, easy to deploy and test.

## Features
- Minimal endpoints:
  - `/` returns a simple OK
  - `/ping` returns `{"pong": true}`
  - `/ip` shows the client IP the server sees
  - `/headers` echoes request headers (handy for debugging LB/proxy headers)
- Tiny dependency footprint (`fastapi`, `uvicorn`)

## Quickstart

### Requirements
- Python 3.10+ recommended

### Install and run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run (quiet server logs)
uvicorn app.simple:app --host 0.0.0.0 --port 8000 --reload --no-access-log
```

### Verify endpoints
```bash
curl -i http://127.0.0.1:8000/
curl -i http://127.0.0.1:8000/ping
curl -i http://127.0.0.1:8000/ip
curl -i http://127.0.0.1:8000/headers
```

Expected:
- `/` → 200 with `{"ok": true}`
- `/ping` → 200 with `{"pong": true}`
- `/ip` → 200 with your client IP (useful behind proxies)
- `/headers` → 200 with a JSON dump of request headers

## API

- GET `/`
  - 200: `{"ok": true}`
- GET `/ping`
  - 200: `{"pong": true}`
- GET `/ip`
  - 200: `{"ip": "<client-ip>"}` (as seen by the app)
- GET `/headers`
  - 200: `{"headers": {...}}`

## Project structure
.
├── app/
│ └── simple.py # minimal FastAPI app
└── requirements.txt # fastapi + uvicorn
