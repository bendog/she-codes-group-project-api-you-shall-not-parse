# Generated by Django 4.0.2 on 2022-05-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_eventmodulerole_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodulerole',
            name='event',
        ),
    ]
