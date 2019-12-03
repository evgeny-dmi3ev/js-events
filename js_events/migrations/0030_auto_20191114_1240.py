# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-14 12:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('js_events', '0029_event_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='visual2',
            field=filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_2', to=settings.FILER_IMAGE_MODEL, verbose_name='image 2'),
        ),
        migrations.AlterField(
            model_name='event',
            name='locations',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_locations.Location', verbose_name='locations'),
        ),
        migrations.AlterField(
            model_name='event',
            name='services',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_services.Service', verbose_name='services'),
        ),
        migrations.AlterField(
            model_name='eventrelatedplugin',
            name='related_categories',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='aldryn_categories.Category', verbose_name='related categories'),
        ),
        migrations.AlterField(
            model_name='eventrelatedplugin',
            name='related_hosts',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='aldryn_people.Person', verbose_name='related hosts'),
        ),
        migrations.AlterField(
            model_name='eventrelatedplugin',
            name='related_locations',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_locations.Location', verbose_name='related locations'),
        ),
        migrations.AlterField(
            model_name='eventrelatedplugin',
            name='related_services',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_services.Service', verbose_name='related services'),
        ),
        migrations.AlterField(
            model_name='eventrelatedplugin',
            name='related_types',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_events.EventsConfig', verbose_name='related sections'),
        ),
        migrations.AlterField(
            model_name='relatedspeakersplugin',
            name='speakers',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_events.Speaker', verbose_name='speakers'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='visual',
            field=filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_1', to=settings.FILER_IMAGE_MODEL, verbose_name='image 1'),
        ),
    ]