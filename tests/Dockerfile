# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /tests
WORKDIR /tests

# Copy the requirements file into the container at /tests
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test_api.py file into the container at /tests
COPY test_api.py .

# Run pytest when the container launches
CMD ["pytest"]
