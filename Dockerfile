# syntax=docker/dockerfile:1.7
FROM python:3.13-slim AS base

# -------------------------
# Environment settings
# -------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_CACHE_DIR=/root/.cache/pip

# -------------------------
# System dependencies
# -------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

# -------------------------
# Create non-root user
# -------------------------
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /app

# -------------------------
# Install Python dependencies (layer caching)
# -------------------------
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# -------------------------
# Copy project code
# -------------------------
COPY . /app

# -------------------------
# Set environment for models
# -------------------------
ENV MODEL_DIR=/app/model

# -------------------------
# Switch to non-root
# -------------------------
USER appuser

# -------------------------
# Default command (API)
# -------------------------
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
