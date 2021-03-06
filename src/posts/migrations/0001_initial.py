# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-24 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('body', models.TextField(blank=True, max_length=500)),
                ('pic', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.image_upload_location, width_field='width_field')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
