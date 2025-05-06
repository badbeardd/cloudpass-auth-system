# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt from the correct path
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual app code
COPY backend/app/ .

# Expose FastAPI port
EXPOSE 8000

# Run the app
CMD ["python", "-m", "main"]
