# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181121_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('can_add_organization_user', 'Can Add New User'), ('can_edit_organization_user_permission', 'Can Edit Users Permissions'))},
        ),
    ]