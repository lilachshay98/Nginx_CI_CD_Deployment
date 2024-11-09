# Use an official Python image from Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the test script into the container
COPY test.py /app/test.py

# Run the test script
CMD ["sh", "-c", "pytest -s test_login.py --env=stag && pytest -s test_send_ecard.py --env=stag"] 
