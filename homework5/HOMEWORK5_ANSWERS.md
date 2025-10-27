# Homework 5 - Deployment - Answers

## Question 1: uv Version
**Answer: uv 0.9.5**

Installation command:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Question 2: First Hash for Scikit-Learn 1.6.1
**Answer:** 
```
sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e
```

This is the hash for the source distribution (sdist) in the `uv.lock` file.

Commands used:
```bash
uv init homework5
cd homework5
uv add "scikit-learn==1.6.1"
```

## Question 3: Load Pipeline and Score
**Answer: 0.533** (closest option)

Actual value: 0.534

Record scored:
```json
{
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}
```

Script: `predict.py`

## Question 4: FastAPI Service
**Answer: 0.534** (closest option)

Client scored:
```json
{
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
```

Files created:
- `app.py` - FastAPI application
- `test_client.py` - Test script

Run with:
```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8000
```

## Question 5: Docker Base Image Size
**STATUS: Docker not installed on this system**

To complete:
1. Install Docker Desktop for Windows
2. Run: `docker pull agrigorev/zoomcamp-model:2025`
3. Run: `docker images`
4. Check the SIZE column

Expected answer options:
- 45 MB
- 121 MB
- 245 MB
- 330 MB

## Question 6: Docker Container with FastAPI
**STATUS: Docker not installed on this system**

To complete:
1. Build: `docker build -t homework5-fastapi .`
2. Run: `docker run -d -p 8000:8000 homework5-fastapi`
3. Test: `uv run test_docker.py`

Expected answer options:
- 0.39
- 0.59
- 0.79
- 0.99

Files created:
- `Dockerfile`
- `test_docker.py`
- `DOCKER_INSTRUCTIONS.md`

## Summary

### Completed:
- ✅ Question 1: uv 0.9.5
- ✅ Question 2: sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e
- ✅ Question 3: 0.533
- ✅ Question 4: 0.534

### Requires Docker Installation:
- ⏳ Question 5: Need to check image size
- ⏳ Question 6: Need to run Docker container

### Project Structure:
```
homework5/
├── app.py                      # FastAPI application
├── predict.py                  # Simple prediction script
├── test_client.py              # Test script for FastAPI
├── test_docker.py              # Test script for Docker container
├── Dockerfile                  # Docker configuration
├── DOCKER_INSTRUCTIONS.md      # Detailed Docker instructions
├── HOMEWORK5_ANSWERS.md        # This file
├── pipeline_v1.bin             # Trained model (downloaded)
├── pyproject.toml              # Project dependencies
└── uv.lock                     # Lock file with hashes
```

