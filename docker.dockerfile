{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9aa5025-1a4e-4fc8-b48a-af322f074ef1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dockerfile\n",
    "\n",
    "# Use an official Python runtime as a parent image\n",
    "FROM python:3.9-slim\n",
    "\n",
    "# Set the working directory in the container\n",
    "WORKDIR /app\n",
    "\n",
    "# Install any needed dependencies\n",
    "COPY requirements.txt /app/\n",
    "RUN pip install --no-cache-dir -r requirements.txt\n",
    "\n",
    "# Copy the current directory contents into the container\n",
    "COPY . /app/\n",
    "\n",
    "# Expose the port the app runs on\n",
    "EXPOSE 5000\n",
    "\n",
    "# Define environment variable to specify the model file path\n",
    "ENV MODEL_PATH /app/model.joblib\n",
    "\n",
    "# Run the Flask app when the container launches\n",
    "CMD [\"python\", \"app.py\"]\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
