#!/bin/sh

set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run the uWSGI server
uwsgi --socket :8000 --master --enable-threads --module employee_roster_2.wsgi:application
