# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the local Python script into the container's working directory
COPY 1024.py .

# Install any necessary dependencies (in this case, just Python 3)
# No additional packages needed for the basic script.
# But if you were using libraries like 'pygame' or others, you could install them here.
# RUN pip install pygame  # Uncomment if you want a graphical version of the game

# Set the environment variable for non-interactive mode
ENV PYTHONUNBUFFERED=1

# Run the Python script
CMD ["python3", "./1024.py"]
