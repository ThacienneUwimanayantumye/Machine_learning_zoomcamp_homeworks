# Homework 5 - Deployment with uv, FastAPI, and Docker

This project implements a lead scoring API using FastAPI and demonstrates deployment with Docker.

## Quick Start

### 1. Install uv (if not already installed)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Install Dependencies
```bash
cd homework5
uv sync
```

### 3. Run the FastAPI Application
```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8000
```

### 4. Test the API
In a new terminal:
```bash
uv run test_client.py
```

## Files

- **app.py** - FastAPI application that serves the ML model
- **predict.py** - Simple script to test model predictions
- **test_client.py** - Script to test the FastAPI endpoint
- **test_docker.py** - Script to test the Dockerized API
- **Dockerfile** - Docker configuration for deployment
- **pipeline_v1.bin** - Pre-trained ML pipeline
- **HOMEWORK5_ANSWERS.md** - Complete homework answers
- **DOCKER_INSTRUCTIONS.md** - Detailed Docker setup instructions

## API Endpoints

### GET /
Health check endpoint

### POST /predict
Predict conversion probability for a lead

Request body:
```json
{
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
```

Response:
```json
{
    "probability": 0.534
}
```

## Docker Deployment

### Build
```bash
docker build -t homework5-fastapi .
```

### Run
```bash
docker run -d -p 8000:8000 homework5-fastapi
```

### Test
```bash
uv run test_docker.py
```

## Homework Answers

1. **uv version**: 0.9.5
2. **First Scikit-Learn hash**: sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e
3. **Prediction for paid_ads client**: 0.533
4. **Prediction for organic_search client**: 0.534
5. **Docker image size**: (requires Docker installation)
6. **Docker prediction**: (requires Docker installation)

See `HOMEWORK5_ANSWERS.md` for detailed answers and `DOCKER_INSTRUCTIONS.md` for Docker setup.

