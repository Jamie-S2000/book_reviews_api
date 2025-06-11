release: python manage.py makemigrations && python manage.py migrate
web: gunicorn book_reviews_api.wsgi --log-file -