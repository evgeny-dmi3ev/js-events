# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-21 12:33
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations
import django.db.models.deletion
from django.apps import apps as django_apps

def forward(apps, schema_editor):
    #Event = django_apps.get_model('js_events.Event')
    #from cms.models import Placeholder

    #placeholder_names = ['content', 'registration_content', 'sidebar']
    #for event in Event.objects.all():
        #for placeholder_name in placeholder_names:
            #placeholder_id_name = '{0}_id'.format(placeholder_name)
            #placeholder_id = getattr(event, placeholder_id_name, None)
            #if placeholder_id is not None:
                #continue
            #placeholder_new = Placeholder.objects.create(slot=placeholder_name)
            #setattr(event, placeholder_id_name, placeholder_new.pk)
        #event.save()
    pass

def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('js_events', '0024_event_sidebar'),
    ]

    operations = [
        migrations.RunPython(forward, backwards)
    ]
