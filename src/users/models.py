# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from organizations.models import Organization

# Create your models here.


def image_upload_location(instance, filename):
    return "Profile_pictures/{}/{}".format(instance.username, filename)

class CustomUser(AbstractUser):
    bio          = models.TextField(max_length=500, blank=True)
    birth_date   = models.DateField(null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name="users", null=True, blank=True)
    is_owner     = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to = image_upload_location,
                            null=True , blank=True,
                            width_field = "width_field",
                            height_field = "height_field",)

    width_field  = models.IntegerField(default= 0)
    height_field = models.IntegerField(default= 0)

    class Meta :
        permissions = (
            ("can_add_organization_user", "Can Add New User"),
        )
