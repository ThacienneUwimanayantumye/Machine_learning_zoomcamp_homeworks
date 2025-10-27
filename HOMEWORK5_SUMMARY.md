# Homework 5 Completion Summary

## ✅ Completed Questions (1-4)

### Question 1: uv Version
**Answer: `uv 0.9.5`**

### Question 2: First Hash for Scikit-Learn 1.6.1
**Answer:** 
```
sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e
```

### Question 3: Model Prediction for paid_ads Client
**Answer: 0.533** (closest option)
- Actual value: 0.534
- Client: `{"lead_source": "paid_ads", "number_of_courses_viewed": 2, "annual_income": 79276.0}`

### Question 4: FastAPI Service Prediction
**Answer: 0.534** (closest option)
- Client: `{"lead_source": "organic_search", "number_of_courses_viewed": 4, "annual_income": 80304.0}`

## ⏳ Requires Docker Installation (Questions 5-6)

### Question 5: Docker Base Image Size
**Status:** Docker not installed - Need to install Docker Desktop for Windows

To complete after installing Docker:
```bash
docker pull agrigorev/zoomcamp-model:2025
docker images
```
Look for the SIZE column (expected: 121 MB or 245 MB based on typical Python slim images)

### Question 6: Docker Container Prediction
**Status:** All files prepared - Ready to build and run after Docker installation

To complete after installing Docker:
```bash
cd homework5
docker build -t homework5-fastapi .
docker run -d -p 8000:8000 homework5-fastapi
uv run test_docker.py
```

## 📁 Project Structure

All homework files are in: `homework5/`

Key files:
- ✅ `app.py` - FastAPI application (working)
- ✅ `predict.py` - Simple prediction script (tested)
- ✅ `test_client.py` - API test script (tested)
- ✅ `test_docker.py` - Docker test script (ready)
- ✅ `Dockerfile` - Docker configuration (prepared)
- ✅ `pipeline_v1.bin` - Downloaded model (verified checksum)
- ✅ `pyproject.toml` & `uv.lock` - Dependencies installed

Documentation:
- ✅ `README.md` - Quick start guide
- ✅ `HOMEWORK5_ANSWERS.md` - Detailed answers
- ✅ `DOCKER_INSTRUCTIONS.md` - Docker setup guide

## 🚀 Next Steps

1. **Install Docker Desktop for Windows**
   - Download from: https://www.docker.com/products/docker-desktop/
   - Follow installation instructions
   - Restart your computer if required

2. **Complete Question 5:**
   ```bash
   docker pull agrigorev/zoomcamp-model:2025
   docker images
   ```
   Record the size from the SIZE column.

3. **Complete Question 6:**
   ```bash
   cd homework5
   docker build -t homework5-fastapi .
   docker run -d -p 8000:8000 homework5-fastapi
   uv run test_docker.py
   ```
   Record the probability from the output.

## 📝 Submission

Submit answers here: https://courses.datatalks.club/ml-zoomcamp-2025/homework/hw05

### Current Answers:
1. ✅ uv 0.9.5
2. ✅ sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e
3. ✅ 0.533
4. ✅ 0.534
5. ⏳ [Need Docker] - Expected: 121 MB or 245 MB
6. ⏳ [Need Docker] - Expected: 0.59 or 0.79

## 🎯 Status: 4/6 Questions Complete

The homework is **66% complete**. Questions 1-4 are fully answered and tested. Questions 5-6 require Docker installation but all necessary files and scripts are prepared and ready to use.

