#!/bin/bash
echo "Build script started..."
pip install -r requirements.txt
echo "Dependencies installed."
python manage.py collectstatic --noinput --clear
mkdir -p staticfiles  # Ensure the staticfiles directory exists even if collectstatic finds nothing.
echo "Static files collected (if any)."
echo "Build complete."
