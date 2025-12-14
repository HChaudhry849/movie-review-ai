FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy everything in the build context into /app/dashboard
COPY . /app/dashboard

RUN chmod +x /app/dashboard/entrypoint.sh

EXPOSE 8501

ENTRYPOINT ["bash", "/app/dashboard/entrypoint.sh"]