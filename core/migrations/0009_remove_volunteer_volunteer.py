# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_volunteer_volunteer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='volunteer',
        ),
    ]