# Generated by Django 4.2.16 on 2024-11-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
    ]
