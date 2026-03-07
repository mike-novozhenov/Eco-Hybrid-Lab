# Use the official Microsoft Playwright image as it already has all OS dependencies
FROM mcr.microsoft.com/playwright/python:v1.49.0-noble

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (chromium only)
RUN playwright install chromium

# Copy the rest of the project files
COPY . .

# Command to run tests and generate reports
CMD ["pytest", "--alluredir=allure-results"]