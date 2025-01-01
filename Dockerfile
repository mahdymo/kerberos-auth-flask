# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y nginx krb5-user \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy NGINX configuration
COPY ./nginx/kerberos-auth-flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/kerberos-auth-flask.conf /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default

# Expose NGINX ports
EXPOSE 80
EXPOSE 443

# Start services
CMD ["/bin/sh", "-c", "service nginx start && gunicorn --workers 4 --bind 0.0.0.0:5000 app:app"]
