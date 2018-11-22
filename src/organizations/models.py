# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.urls import reverse
import random


def file_upload_location(instance, filename):
    return "Auth_pictures/{}/{}".format(instance.name, filename)
def image_upload_location(instance, filename):
    return "Profile_pictures/{}/{}".format(instance.name, filename)
    
class Organization(models.Model):
    owner_id    = models.IntegerField(default = 1)
    name        = models.CharField(max_length=30, blank=True)
    bio         = models.TextField(max_length=500, blank=True)
    location    = models.CharField(max_length=30, blank=True)
    logo        = models.FileField(upload_to = image_upload_location,
                                      null=True,
                                      blank=True,)
    auth_image  = models.FileField(upload_to = file_upload_location,
                                      null=True,
                                      blank=True,
                                      help_text= "Add Your Authorization Pdf")
    slug        = models.SlugField(null=True , blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organizations:organizations-detail" , kwargs={"slug" : self.slug})

def pre_save_organization(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug  = slugify(instance.name)+'-'+str(random.randint(1,1000000000))
pre_save.connect(pre_save_organization, Organization)

# def organization_owner(instance, *args, **kwargs):
#     user_id = instance.owner_id
#     instance.users.create()
# pre_save.connect(organization_owner, Organization)



# class OrganizationGroup(models.Model):
#     organization = models.OneToOneField(Organization, on_delete=models.CASCADE,)
#
#     def __str__(self):
#         return self.organization.name
#
# def pre_save_organizationgroup(instance, *args, **kwargs):
#     orgGroup = OrganizationGroup.objects.get_or_create(organization = instance)
# pre_save.connect(pre_save_organizationgroup, Organization)
