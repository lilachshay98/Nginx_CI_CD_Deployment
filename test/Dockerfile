# Use an official Python image from Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the test script into the container
COPY test.py /app/test.py

# Run the test script
CMD ["python", "/app/test.py"]
