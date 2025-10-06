# Start from a official slim Python image
FROM python:3.11-slim
# Set work directory in container
WORKDIR /app
# Copy backend files
COPY . /app
# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt
# App listens on port 5000
EXPOSE 5000
# Start Flask whenthe container runs
CMD ["python", "app.py"]
