# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserCreateForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm # should be add_form and UserCreationForm
    change_form = UserChangeForm # should be change_form and UserChangeForm
    model = CustomUser
    list_display = ['username', 'organization', 'id', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)
