# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0029_auto_20160622_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]