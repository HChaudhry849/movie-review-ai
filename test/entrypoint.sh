#!/bin/bash
set -e

# Wait for Flask to be healthy
until curl -fs http://flask-service:5000/health; do
  echo "Waiting for Flask..."
  sleep 3
done

# Run Playwright tests
npx playwright test