web: gunicorn oc_lettings_site.wsgi
release: python manage.py migrate
release: python manage.py loaddata db.json
