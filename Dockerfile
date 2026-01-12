# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY student.py .
COPY test_student.py .

# Run unit tests during build (CI friendly)
RUN python -m unittest test_student.py

# Default command to run the application
CMD ["python", "student.py"]
