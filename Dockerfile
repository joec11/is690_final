# Define a base stage with a Debian Bookworm base image that includes the latest glibc update
FROM python:3.12-bookworm AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=true \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    QR_CODE_DIR=/myapp/qr_codes

WORKDIR /myapp

# Update system and specifically upgrade libc-bin, libsystemd0, and libudev1 to their latest versions
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    libc-bin \
    libsystemd0 \
    libudev1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies in /.venv
COPY requirements.txt .
RUN python -m venv /.venv \
    && . /.venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Define a second stage for the runtime, using the same Debian Bookworm slim image
FROM python:3.12-slim-bookworm AS final

# Upgrade libc-bin, libsystemd0, and libudev1 in the final stage to their latest versions
RUN apt-get update && apt-get install -y --no-install-recommends \
    libc-bin \
    libsystemd0 \
    libudev1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from the base stage
COPY --from=base /.venv /.venv

# Set environment variable to ensure all python commands run inside the virtual environment
ENV PATH="/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    QR_CODE_DIR=/myapp/qr_codes

# Set the working directory
WORKDIR /myapp

# Create and switch to a non-root user
RUN useradd -m myuser
USER myuser

# Copy application code with appropriate ownership
COPY --chown=myuser:myuser . .

# Expose port 8080 to allow external access to the application running inside the container
EXPOSE 8080

# Set the entrypoint for the container. This specifies the executable that should be run when the container starts.
# Here, we use 'uvicorn' as the entrypoint, which is a high-performance ASGI server for running FastAPI applications.
ENTRYPOINT ["uvicorn"]

# Define the default command to run with the entrypoint.
# This command specifies the application module and configuration for running the server.

# Development Configuration:
# Uncomment the following line to enable the development mode with live reloading.
# This is useful during development to automatically apply code changes without restarting the server.
# CMD ["app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

# Production Configuration:
# The default command for production environments does not include the `--reload` flag.
# This should be used in a production setting for better performance and stability.
# The application will listen on all interfaces (`--host 0.0.0.0`) and port 8080.
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8080"]
