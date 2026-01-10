# Use a minimal Python base image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install Python dependencies
ENV UV_PROJECT_ENVIRONMENT=/usr/local
RUN uv sync

# Copy application code
COPY . .

# Copy trained models into the image
COPY ./model /app/model

# Expose the application port
EXPOSE 8000

# Run the FastAPI application
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]