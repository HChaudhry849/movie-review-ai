FROM python:3.8-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Prepare folders
RUN mkdir -p data/ train/ evaluate/ models/

# Copy project files
COPY train/ train/
COPY scripts/ scripts/

# Make entrypoint executable
RUN chmod +x ./scripts/run_pipeline.sh

# Run the pipeline on container start
ENTRYPOINT ["./scripts/run_pipeline.sh"]