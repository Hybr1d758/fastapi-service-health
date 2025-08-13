FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# System deps (optional minimal)
RUN adduser --disabled-password --gecos '' appuser

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

USER appuser
EXPOSE 8000

CMD ["uvicorn", "app.simple:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]


