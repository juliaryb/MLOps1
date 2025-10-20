# Dockerfile

# Use a minimal Python image as the base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH"

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only dependency files first (to leverage caching)
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv
ENV UV_PROJECT_ENVIRONMENT=/usr/local
RUN uv sync

# Copy the rest of the application code
COPY . . 

# Expose the application port
EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]