#!/bin/bash

# Start FastAPI backend
uvicorn backend.app:app --host 0.0.0.0 --port 8000 &

# Start Node frontend
cd frontend && npm start
