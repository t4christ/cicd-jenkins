web: gunicorn t4c.wsgi --timeout 15 --keep-alive 5 --log-file -
worker: celery -A t4c worker --loglevel=info 