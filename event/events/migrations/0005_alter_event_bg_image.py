# Generated by Django 5.1.2 on 2024-10-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_options_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/%Y/%m/%d/', verbose_name='Картинка мероприятия'),
        ),
    ]
