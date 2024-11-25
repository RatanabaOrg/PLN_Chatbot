# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency files to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the required NLTK corpora
RUN python -m nltk.downloader mac_morpho

# Copy the rest of the project files to the container
COPY . .

# Expose the port where Flask will run
EXPOSE 5000

# Set the command to run the Flask server
CMD ["python", "app.py"]
