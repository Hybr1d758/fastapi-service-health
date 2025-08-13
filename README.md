
## FastAPI Network Test Service

A minimal FastAPI service to quickly test networking, routing, and headers in local or cloud environments.

### Why this is useful 
- Load balancer/ingress health checks: Point probes to /ping to validate target health and routing.
- Network reachability tests: Quickly confirm a service is reachable on host/port in different environments.
- Proxy/header debugging: Use /headers to see what headers survive through gateways (X-Forwarded-For, auth).
- Client IP verification: /ip shows what the app sees (useful with NAT, reverse proxies, WAFs).
- CI/CD smoke tests: Post-deploy curl /ping to fail fast if the service isn’t reachable.

## Features
- Minimal endpoints:
  - `/` returns OK
  - `/ping` returns `{"pong": true}`
  - `/ip` shows client IP
  - `/headers` echoes request headers
  - `/time` returns current UTC time (ISO 8601, epoch ms)
- Tiny deps: `fastapi`, `uvicorn`
- Tests with `pytest`
- Dockerfile for containerized runs
- GitHub Actions CI (install + tests on PRs and pushes)
- Makefile for common tasks

## Quickstart

### Requirements
- Python 3.10+

### Install and run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

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
- `/` → `{"ok": true}`
- `/ping` → `{"pong": true}`
- `/ip` → `{"ip": "<client-ip>"}` (as seen by the app)
- `/headers` → `{"headers": {...}}`
- `/time` → `{"iso_utc": "...", "epoch_ms": 1234567890}`

## Makefile 
```bash
make run        # start the app (uvicorn)
make test       # run pytest
make build      # build Docker image
make docker-run # run container on port 8000
```

## Testing
```bash
pip install -r requirements.txt
pytest -q
```

## Docker
```bash
docker build -t fastapi-network-test .
docker run --rm -p 8000:8000 fastapi-network-test
```

## CI (GitHub Actions)
- Workflow: `.github/workflows/ci.yml`
- Runs on pushes to `dev`/`main` and PRs to `main`
- Steps: setup Python → install deps → run tests

## API
- GET `/` → `{"ok": true}`
- GET `/ping` → `{"pong": true}`
- GET `/ip` → `{"ip": "<client-ip>"}`
- GET `/headers` → `{"headers": {...}}`
- GET `/time` → `{"iso_utc": "...", "epoch_ms": ...}`

## Project structure
```
 .
 ├── app/
 │ └── simple.py
 ├── tests/
 │ └── test_simple.py
 ├── .github/
 │ └── workflows/
 │ └── ci.yml
 ├── Dockerfile
 ├── Makefile
 ├── requirements.txt
 └── README.md
