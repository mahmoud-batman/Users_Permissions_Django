# from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'', addNewPost, name='add-new-post'),
]
