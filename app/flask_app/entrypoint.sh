#!/bin/bash
set -e

echo "$(date -Is) [FLASK] Waiting for training to complete..."

while [ ! -f /app/data/training.complete ]; do
    sleep 5
done

echo "$(date -Is) [FLASK] Training complete. Starting Flask..."

# Move into the folder where app.py lives
cd /app/flask_app || exit

exec python3 app.py