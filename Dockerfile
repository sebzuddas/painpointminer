# Backend Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install uv
RUN uv pip install --system -r requirements.txt
COPY . .

CMD ["uvicorn", "painpointsite.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"] 