FROM python:3.8-slim
# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app/flask_app/  
# Make entrypoint executable
RUN chmod +x /app/flask_app/entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["bash", "/app/app/flask_app/entrypoint.sh"]