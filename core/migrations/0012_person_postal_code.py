# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170409_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='postal_code',
            field=models.TextField(blank=True, default='', verbose_name='Código postal'),
        ),
    ]