# Use official Python image
FROM python:3.13-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY . /app/
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run the app
CMD ["fastapi", "run", "main.py"]