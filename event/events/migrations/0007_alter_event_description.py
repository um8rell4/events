# Generated by Django 5.1.2 on 2024-10-29 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=10000, verbose_name='Описание ивентa'),
        ),
    ]