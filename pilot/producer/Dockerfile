# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY src/ src/
COPY ./main.py /app
# COPY config/ config/

ENV PYTHONPATH /app/src
# Set the environment variable for the config file location
# ENV CONFIG_PATH=/app/config/.env

# Run the application
CMD ["python", "main.py"]