FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app/ollama/

RUN chmod +x /app/ollama/entrypoint.sh

# ENTRYPOINT ensures that this script ALWAYS runs when the container starts.
# Unlike CMD, which can be overridden if someone passes a different command to `docker run`,
# ENTRYPOINT guarantees that the container will execute this script no matter what.
# Any extra arguments passed during `docker run` will be passed to the script as parameters.
# 
# In our case, this is crucial because:
# 1. The script generates the training CSV.
# 2. It creates the `training.done` file that signals the training-service to start.
# 3. We rely on this process completing every time, so we can’t risk the script being skipped.
ENTRYPOINT ["/app/ollama/entrypoint.sh"]