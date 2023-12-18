# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Install Apache Benchmark (ab) based on the Linux distribution
RUN apt-get update && apt-get install -y apache2-utils || \
    pacman -Syu --noconfirm apache-tools || \
    pacman -Syu --noconfirm apache || \
    apk --no-cache add apache2-utils

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]