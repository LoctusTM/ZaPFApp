# Deployment Notes

## Datenbank migrieren

```
cd app
python manage.py makemigrations timetable
python manage.py migrate
```

## Start Testserver

```
python manage.py runserver
```

## Start using Gunicorn

```
/home/user/ZaPFApp/venv/bin/gunicorn --workers 3 --bind unix:/home/user/ZaPFApp/app/zapfapp.sock app.wsgi:application
```
Using Gunicorn installed in venv


## Systemd Service File (Example)

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=lennart
Group=www-data
WorkingDirectory=/home/lennart/ZaPFApp/app
ExecStart=/home/lennart/ZaPFApp/venv/bin/gunicorn --workers 3 --bind unix:/home/lennart/ZaPFApp/app/zapfapp.sock app.wsgi:application

[Install]
WantedBy=multi-user.target
```

## Nginx example configuration

```

server {
    listen 80;
    listen [::]:80;
    server_name app.zapfinhd.de;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    include /etc/nginx/snippets/letsencrypt.conf;
    include /etc/nginx/snippets/ethylomat.conf;
    include /etc/nginx/snippets/ssl.conf;

    access_log /var/log/nginx/zapfapp-access.log;
    error_log  /var/log/nginx/zapfapp-error.log;

    server_name app.zapfinhd.de;
    root /home/user/ZaPFApp;


    location /static/ {
        root /home/user/ZaPFApp/app/timetable;
    }

    location /static/admin/ {
        root /home/user/ZaPFApp/venv/lib/python3.5/site-packages/django/contrib/admin;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user/ZaPFApp/app/zapfapp.sock;
    }

    location ~ /.well-known {
        allow all;
    }

    client_max_body_size 50m;
}

```

