# Generated by Django 4.2.16 on 2024-11-06 12:48

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='profile_images/default.jpg', upload_to=users.models.user_directory_path, verbose_name='Картинка пролфиля'),
        ),
    ]