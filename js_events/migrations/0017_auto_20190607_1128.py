# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-07 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_events', '0016_auto_20190607_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Event Price'),
        ),
    ]
