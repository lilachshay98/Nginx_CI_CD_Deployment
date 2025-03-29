# Use an official Python image from Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the test script into the container
# COPY test.py /app/test.py

# Set the command to run the test script
CMD ["python", "test.py"]
