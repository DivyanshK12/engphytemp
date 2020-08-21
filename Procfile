web: gunicorn wsgi:app
release: python manage.py db init
release: python manage.py db migrate -m 'initial'
release: python manage.py db upgrade
