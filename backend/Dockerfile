# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

COPY .env .

# Make sure your start.sh script is executable
RUN chmod +x start.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Use start.sh to run the app
CMD ["./start.sh"]