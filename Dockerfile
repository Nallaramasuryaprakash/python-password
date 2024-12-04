# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Flask (and other dependencies if needed)
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "password_generator.py"]
