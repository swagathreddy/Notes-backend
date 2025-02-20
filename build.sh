#!/bin/bash
# Install system dependencies
apt-get update
apt-get install -y default-libmysqlclient-dev pkg-config build-essential python3-dev

# Set up virtual environment and install Python packages
python -m venv /opt/venv
source /opt/venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate
