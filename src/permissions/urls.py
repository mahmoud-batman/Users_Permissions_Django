# from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/create-permissions/$' ,  createPermissions ,name="create-permissions" ) ,
    url(r'^(?P<pk>\d+)/edit/$' ,  editPermissions ,name="edit-permissions" ) ,
]
