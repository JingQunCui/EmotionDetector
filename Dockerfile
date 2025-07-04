# Base image
FROM python:3.12-slim as backend

# Backend setup
WORKDIR /app
COPY backend/ ./backend/
COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Frontend (Node.js) setup
FROM node:18 AS frontend

WORKDIR /app
COPY frontend/ ./frontend/
RUN cd frontend && npm install

# Final stage: combine both
FROM python:3.12-slim

# Copy backend
WORKDIR /app
COPY --from=backend /app/backend ./backend 
COPY --from=backend /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=backend /usr/local/bin /usr/local/bin

# Copy frontend
COPY --from=frontend /app/frontend ./frontend

# Install required OS packages
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install Node.js (already in path from frontend layer)
ENV PATH="/usr/local/bin:$PATH"

# Expose ports
EXPOSE 3000 8000

# Start both backend and frontend
COPY start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]
