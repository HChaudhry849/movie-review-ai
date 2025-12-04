FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
#mkdir creates empty folders, COPY copies files from host to container
#We need to create these folders so that the container has them ready to use
RUN mkdir -p app/data/
COPY train/ app/train/
RUN mkdir -p app/evaluate/
RUN mkdir -p app/models/
COPY scripts/ scripts/
CMD ["./scripts/run_pipeline.sh"]