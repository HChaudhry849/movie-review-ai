FROM ollama/ollama:latest

# Copy your model file if needed (optional)

# Start Ollama and pull the model inside ENTRYPOINT script
ENTRYPOINT ["/bin/bash", "-c", "\
    ollama serve & \
    sleep 5 && \
    ollama pull gemma3:4b && \
    wait \
"]

EXPOSE 11434