# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181121_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]
