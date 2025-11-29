FROM python:3.8-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY data/ app/data/
COPY train/ app/train/
COPY evaluate/ app/evaluate/
COPY models/ app/models/
COPY scripts/ scripts/
CMD ["./scripts/run_pipeline.sh"]