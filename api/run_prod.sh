#!/bin/bash

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Install/upgrade dependencies
pip install -r requirements.txt

# Set environment variables
export PORT=${PORT:-8000}
export GROQ_API_KEY=${GROQ_API_KEY}

# Start Gunicorn
exec gunicorn -c gunicorn_config.py main:app 