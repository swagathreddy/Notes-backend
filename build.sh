#!/bin/bash
# Install system dependencies
apt-get update
apt-get install -y default-libmysqlclient-dev pkg-config build-essential python3-dev

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate
