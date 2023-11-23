# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--port", "8000", "--host", "localhost"]