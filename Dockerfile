# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variable for the model and task
ARG MODEL_NAME
ENV MODEL_NAME=${MODEL_NAME}
ARG TASK_NAME
ENV TASK_NAME=${TASK_NAME}

# Echo the model and task names (useful for debugging)
RUN echo "Model Name: $MODEL_NAME"
RUN echo "Task Name: $TASK_NAME"

# Set the working directory in the container
WORKDIR /usr/src/app

# Echo the working directory
RUN echo "Working directory set to /usr/src/app"

# Copy the current directory contents into the container at /usr/src/app
COPY ./app .

# Echo after copying files
RUN echo "Copied project files to /usr/src/app"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    echo "Successfully installed requirements"

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Echo environment variable
RUN echo "Environment NAME set to $NAME"

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
