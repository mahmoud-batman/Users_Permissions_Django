# from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^create/$' ,  organizationsCreate ,name="create" ) ,
    url(r'^organization/$' ,  myOrganizationsList ,name="myorganizations-list" ) ,
    url(r'^myadmin/organization-list/$', organizationsList , name='organizations-list'), # Admin
    url(r'^(?P<slug>[-\w]+)/detail/$', organizationDetail ,name="organizations-detail"),
    url(r'^(?P<slug>[-\w]+)/update/$', OrganizationsUpdateView.as_view(),name="update"),

    ]
