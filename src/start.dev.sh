#!/bin/bash

while !</dev/tcp/db/5432; do 
sleep 10
done

python manage.py migrate

exec python manage.py runserver 0.0.0.0:8000