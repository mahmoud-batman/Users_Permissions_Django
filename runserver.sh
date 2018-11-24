#!/bin/bash
source bin/activate
cd src
atom ../ 
python manage.py runserver 
