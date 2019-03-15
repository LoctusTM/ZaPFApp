pip install gunicorn
cd app
gunicorn --log-level debug -b ':80' app.wsgi:application
