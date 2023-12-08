# Use an official Python runtime as a base image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy startup script and grant execution permissions
COPY startup.sh /code/
RUN chmod +x /code/startup.sh

# Run startup script when the container launches
CMD ["/code/startup.sh"]
