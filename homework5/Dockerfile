FROM agrigorev/zoomcamp-model:2025

WORKDIR /code

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install uv
RUN pip install uv

# Install dependencies
RUN uv sync --frozen

# Copy the Docker-specific app (uses pipeline_v2.bin from base image)
COPY app_docker.py ./app.py

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
