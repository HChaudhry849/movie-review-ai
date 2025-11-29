FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY data/ app/data/
COPY train/ app/train/
COPY evaluate/ app/evaluate/
COPY models/ app/models/
COPY scripts/ scripts/
CMD ["./scripts/run_pipeline.sh"]