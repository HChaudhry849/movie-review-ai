#!/bin/bash
set -e

echo "Running ollama data generation…"

# Run your existing Python logic
python /app/ollama_generate.py

echo "Generation completed, creating done file…"

# Create the completion marker, this is just a fine created after the csv is updated. It's a flag to confirm the process is done.
touch /app/data/training.done

# Keep the container alive for healthcheck
sleep infinity