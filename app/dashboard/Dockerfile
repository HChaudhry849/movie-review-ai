FROM python:3.8-slim

# Install curl for health checks
RUN apt-get update \
 && apt-get install -y curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy everything in the build context into /app/app/dashboard
COPY . /app/app/dashboard

# Make entrypoint executable
RUN chmod +x /app/app/dashboard/entrypoint.sh

EXPOSE 8501
ENTRYPOINT ["bash", "/app/app/dashboard/entrypoint.sh"]
