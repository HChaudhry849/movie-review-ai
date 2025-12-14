FROM python:3.8-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy training code (including run_pipeline.sh)
COPY train /app/app/train/

# Copy shared data and evaluation folders
COPY data /app/app/data/
COPY evaluate /app/app/evaluate/

# Copy the pipeline script
COPY run_pipeline.sh /app/app/run_pipeline.sh
# Make the pipeline script executable
RUN chmod +x /app/app/run_pipeline.sh

# Run the pipeline on container start
ENTRYPOINT ["bash", "/app/app/run_pipeline.sh"]
