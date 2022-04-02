web: gunicorn oc_lettings_site.wsgi
release: sh -c 'python manage.py migrate && python manage.py loaddata db.json'