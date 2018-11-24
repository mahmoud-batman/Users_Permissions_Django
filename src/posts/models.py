# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
def image_upload_location(instance, filename):
    return "Posts/{}/{}".format(instance.title, filename)

class Post(models.Model):
    title   = models.CharField(max_length=30, null=True, blank=True)
    body    = models.TextField(max_length=500)
    pic     = models.ImageField(upload_to = image_upload_location,
                            null=True , blank=True,
                            width_field = "width_field",
                            height_field = "height_field",)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
