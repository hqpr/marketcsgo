web: python manage.py collectstatic --noinput
web: python manage.py migrate --noinput
web: gunicorn marketcsgo.wsgi --log-file -