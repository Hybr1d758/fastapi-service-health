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
  - `/time` returns current UTC timestamp (ISO 8601 and epoch ms)
- Tiny dependency footprint (`fastapi`, `uvicorn`)

## Quickstart

### Requirements
- Python 3.10+

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
curl -i http://127.0.0.1:8000/time
```

Expected:
- `/` → 200 with `{"ok": true}`
- `/ping` → 200 with `{"pong": true}`
- `/ip` → 200 with your client IP (useful behind proxies)
- `/headers` → 200 with a JSON dump of request headers
- `/time` → 200 with ISO UTC and epoch ms

## API

- GET `/`
  - 200: `{"ok": true}`
- GET `/ping`
  - 200: `{"pong": true}`
- GET `/ip`
  - 200: `{"ip": "<client-ip>"}` (as seen by the app)
- GET `/headers`
  - 200: `{"headers": {...}}`
- GET `/time`
  - 200: `{"iso_utc": "...", "epoch_ms": 1234567890}`

## Project structure
```
.
├── app/
│   └── simple.py        # minimal FastAPI app
├── requirements.txt     # fastapi + uvicorn
└── README.md
```

## Deploy notes (optional)

### Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

RUN adduser --disabled-password --gecos '' appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
USER appuser
EXPOSE 8000

CMD ["uvicorn", "app.simple:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
```

Build and run:
```bash
docker build -t fastapi-network-test .
docker run --rm -p 8000:8000 fastapi-network-test
```

### Kubernetes (using /ping for probes)
```yaml
livenessProbe:
  httpGet:
    path: /ping
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ping
    port: 8000
  initialDelaySeconds: 3
  periodSeconds: 5
```

## Roadmap (nice-to-have for production)
- Health endpoints (`/live`, `/ready`) with real dependency checks
- Structured JSON logging and correlation IDs (`X-Request-ID`)
- Metrics (`/metrics`) and distributed tracing (OTel)
- CI pipeline (lint + tests + image build)
- Basic rate limiting and security headers

## License
MIT

# fastapi-service-health