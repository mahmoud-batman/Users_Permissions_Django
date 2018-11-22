# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import Organization
# from .forms import OrganizationCreateForm
# # Register your models here.
# #
# class CustomOrganizationAdmin(Organization):
#     add_form = OrganizationCreateForm # should be add_form and UserCreationForm
#     # change_form = UserChangeForm # should be change_form and UserChangeForm
#     model = Organization
#     list_display = [
#             "owner_id",
#             "name",
#             "bio",
#             "location",
#             "auth_image",
#             ]

# admin.site.register(Organization,CustomOrganizationAdmin )
admin.site.register(Organization)
