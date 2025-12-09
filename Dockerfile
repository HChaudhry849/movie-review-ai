FROM python:3.8-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Prepare folders
RUN mkdir -p data/ evaluate/ models/

# Copy project files
COPY app/evaluate/ /app/evaluate/  
COPY app/train/ /app/app/train/   
COPY app/data/ /app/app/data/      
COPY scripts/ /app/scripts/

# Make entrypoint executable
RUN chmod +x /app/scripts/run_pipeline.sh

# Run the pipeline on container start
ENTRYPOINT ["bash", "/app/scripts/run_pipeline.sh"]
