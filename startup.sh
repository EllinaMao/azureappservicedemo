#!/bin/bash

python manage.py migrate core
python manage.py seed_db

gunicorn --bind=0.0.0.0 --timeout 600 project.wsgi
