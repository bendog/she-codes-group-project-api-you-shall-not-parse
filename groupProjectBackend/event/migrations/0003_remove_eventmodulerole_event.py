# Generated by Django 4.0.2 on 2022-06-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodulerole',
            name='event',
        ),
    ]
