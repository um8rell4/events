# Generated by Django 4.2.16 on 2024-11-06 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
