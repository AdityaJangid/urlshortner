# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20170515_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
