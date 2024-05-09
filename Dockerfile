# Use Ubuntu 22 as the base image
FROM ubuntu:22.04

# Set environment variables (you can adjust these as needed)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE pairupbackend.settings

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    postgresql-client

# Create and set the working directory inside the container
WORKDIR /app

# copy the requirements.txt file into the container, for the caching to work effectively
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy your Django project files into the container
COPY . /app/

# Expose port 8000 (the port your Django app will run on)
EXPOSE 8000

# Start the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
