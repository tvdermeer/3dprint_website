# Use an official Python runtime with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.10-bookworm

# Set working directory
WORKDIR /app

# Set environment variables
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Copy dependency files first to leverage Docker cache
COPY pyproject.toml uv.lock ./

# Install dependencies (without the project itself)
# This layer will be cached unless pyproject.toml or uv.lock changes
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . .

# Install the project
RUN uv sync --frozen --no-dev --no-editable

# Expose the port the app runs on
EXPOSE 8000

# Run the application using uv run
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
