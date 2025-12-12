#!/bin/bash
set -e

# Wait for ollama-service to complete
while [ ! -f /app/data/training.done ]; do
    echo "Waiting for /app/data/training.done…"
    sleep 5
done

echo "Starting training pipeline…"

cd /app/app/train || exit

# Point to top level folder for imports
export PYTHONPATH=/app:$PYTHONPATH

python3 main.py

echo "Training pipeline completed."

# Create the completion marker
touch /app/data/training.complete

# Keep the container alive for healthcheck
sleep infinity
