# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-04 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20160602_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='isphoto',
            field=models.BooleanField(default=True),
        ),
    ]
