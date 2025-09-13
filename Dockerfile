FROM python:3.9-slim

LABEL maintainer="Movie-Mate Using Machine Learning Team"
LABEL description="AI-powered movie recommendation system built with Streamlit and Machine Learning"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import streamlit; print('Streamlit OK')" || exit 1

# Run the application
CMD ["streamlit", "run", "movie_mate.py", "--server.port=8501", "--server.address=0.0.0.0"]