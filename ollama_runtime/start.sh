#!/bin/bash

# Start the server in the FRONT (not background-hidden)
ollama serve &
SERVER_PID=$!

# Wait for the server to wake up
until curl -sf http://localhost:11434/api/tags; do
    echo "Waiting for Ollama to start..."
    sleep 1
done

# Pull the model and WAIT for it to finish
echo "Pulling model gemma3:4b..."
ollama pull gemma3:4b
echo "Model ready."

# Keep the server alive
wait $SERVER_PID