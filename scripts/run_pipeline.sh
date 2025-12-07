#!/bin/bash
set -e

# Wait for ollama-service to complete
while [ ! -f /app/data/training.done ]; do
    echo "Waiting for /app/data/training.done…"
    sleep 5
done

echo "Starting training pipeline…"
cd app/train || exit
python3 main.py

echo "Training pipeline completed."

# Create the completion marker, this is just a fine created after the csv is updated. It's a flag to confirm the process is done.
touch /app/data/training.complete

# Keep the container alive for healthcheck
sleep infinity