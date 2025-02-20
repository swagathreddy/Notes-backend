#!/bin/bash

# Install system dependencies for MySQL
apt-get update
apt-get install -y default-libmysqlclient-dev build-essential pkg-config

# Upgrade pip and install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate
