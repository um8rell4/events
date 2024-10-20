from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    profile_picture = models.ImageField(
        default='default.jpg',
        upload_to='media/profile_images',
        verbose_name='Картинка пролфиля'
    )
    is_organizer = models.BooleanField(blank=True, verbose_name='Организатор')
    bio = models.TextField(max_length=250, verbose_name='Описание профиля')
    first_name = models.CharField(max_length=25, verbose_name='Имя')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
