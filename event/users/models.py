from django.db import models
from django.contrib.auth.models import User
from PIL import Image


def user_directory_path(instance, filename):
    # Путь будет выглядеть как 'media/profile_images/username/filename'
    return f'media/profile_images/{instance.user.username}/{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    profile_picture = models.ImageField(
        default='profile_images/default.jpg',
        upload_to=user_directory_path,
        verbose_name='Картинка пролфиля'
    )
    is_organizer = models.BooleanField(verbose_name='Организатор', default=False)
    bio = models.TextField(max_length=250, verbose_name='Описание профиля', blank=True)
    email = models.EmailField(blank=True, verbose_name='email')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path)
