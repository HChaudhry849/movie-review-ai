#!/bin/bash
set -e

# Seed CSV data
mkdir -p /app/data
cp -n /app/seeds/data/* /app/data/

# Seed models
mkdir -p /app/models
cp -n /app/seeds/models/* /app/models/

# Seed evaluate/history.json
mkdir -p /app/evaluate
cp -n /app/seeds/evaluate/history.json /app/evaluate/

echo "Seeding complete."