FROM python:3.8-slim
WORKDIR /app

# Copy seeds into the image
COPY data/ /app/seeds/data/
COPY models/ /app/seeds/models/
COPY evaluate/history.json /app/seeds/evaluate/history.json

# Entrypoint
COPY entrypoint_seed.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]