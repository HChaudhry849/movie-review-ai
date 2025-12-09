FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app/dashboard/  
EXPOSE 8501
CMD ["streamlit", "run", "dashboard/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]