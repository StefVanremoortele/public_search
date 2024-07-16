FROM python:3.9-slim

WORKDIR .

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]
