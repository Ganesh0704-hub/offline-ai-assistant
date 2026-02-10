#!/bin/bash

# Start Ollama (if not already running)
ollama serve >/tmp/ollama.log 2>&1 &

sleep 5

source venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000
