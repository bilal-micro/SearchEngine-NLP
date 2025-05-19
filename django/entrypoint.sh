#!/bin/bash

# Wait for PostgreSQL
echo "⏳ Waiting for Postgres..."
while ! nc -z $DJANGO_DB_HOST 5432; do
  sleep 1
done
echo "✅ Postgres is up"

# Run migrations
echo "🔁 Running migrations..."
python manage.py migrate

# (Optional) Collect static files
# echo "📦 Collecting static files..."
# python manage.py collectstatic --noinput

# Run the Django server in the background
echo "🚀 Starting Django server..."
python manage.py runserver 0.0.0.0:8000 &

# Give the server a moment to start (optional)
sleep 5

# Run your custom script
echo "📥 Running database_loader.py..."
python database_loader.py

# Keep container alive
wait
