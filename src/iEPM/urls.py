"""iEPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', home , name='home'),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^organizations/', include("organizations.urls", namespace="organizations")),
    url(r'^permissions/', include("permissions.urls", namespace="permissions")),
    url(r'^posts/', include("posts.urls", namespace="posts")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
