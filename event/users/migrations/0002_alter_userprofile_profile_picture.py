# Generated by Django 5.1.2 on 2024-10-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_images', verbose_name='Картинка пролфиля'),
        ),
    ]
