# Use a suitable base image
FROM python:3.9-slim

# Set environment variables for proxies
ENV HTTP_PROXY=http://172.24.14.197:3128
ENV HTTPS_PROXY=https://172.24.14.197:3128

# Test network connectivity and install curl
RUN apt-get update && apt-get install -y curl
RUN curl -I https://pypi.tuna.tsinghua.edu.cn/simple

# Copy requirements.txt and print its contents
COPY requirements.txt .
RUN cat requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# Continue with other Dockerfile instructions
