#!/bin/bash

# Wait for PostgreSQL to be ready
python manage.py wait_for_db

# Collect static files say yes
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django app
python manage.py runserver 0.0.0.0:8000
