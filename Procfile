web: gunicorn django_users_management.wsgi --log-file -
release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
