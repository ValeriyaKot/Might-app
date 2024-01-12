python manage.py collectstatic --no-input --clear
python manage.py migrate
gunicorn recognition_platform.wsgi:application --bind 0.0.0.0:8000
