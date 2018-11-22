#!/bin/bash
source ../bin/activate
echo "Enviroment activated ."
dpkg -s django-extensions 2>/dev/null >/dev/null || pip install django-extensions
python manage.py runscript show_urls.py
