#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install and build frontend
cd frontend
npm install
npm run build
cd ..

# Django commands
cd Backend
python manage.py collectstatic --noinput
python manage.py migrate