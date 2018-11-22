# from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'signup/', mySignup, name='signup'),
    url(r'login/', myLogin, name='login'),
    url(r'^myadmin/users-list/', users_list, name='users-list'),
    url(r'myadmin/', myadmin, name='myadmin'),

    url(r'^(?P<slug>[-\w]+)/create-organization-user/$' ,  createOrganizationUser ,name="create-organization-user" ) ,

    url(r'^(?P<pk>\d+)/edit-permissions', userEditPermissions , name='edit-permissions'),
    url(r'^(?P<pk>\d+)/profile/', profile, name='profile'),
]
