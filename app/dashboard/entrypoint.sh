#!/bin/bash
set -e

echo "$(date -Is) [DASHBOARD] Waiting for Flask service to be healthy..."

# Wait for Flask to be ready
while ! curl -fs http://flask-service:5000/health; do
    echo "$(date -Is) [DASHBOARD] Flask not ready yet"
    sleep 5
done

echo "$(date -Is) [DASHBOARD] Flask is ready. Starting dashboard..."
cd /app/dashboard || exit
exec streamlit run /app/dashboard/dashboard.py --server.port=8501 --server.address=0.0.0.0
