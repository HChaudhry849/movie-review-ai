#!/bin/bash
set -e

echo "$(date -Is) [TRAINING] Container started"

while [ ! -f /app/data/training.done ]; do
    echo "$(date -Is) [TRAINING] Waiting for /app/data/training.done"
    sleep 5
done

echo "$(date -Is) [TRAINING] training.done detected"

# Optional: show file metadata
ls -l /app/data/training.done

echo "$(date -Is) [TRAINING] Starting training pipeline"

cd /app/app/train || exit
export PYTHONPATH=/app:$PYTHONPATH

python3 main.py

echo "$(date -Is) [TRAINING] Training completed"

touch /app/data/training.complete
sleep infinity