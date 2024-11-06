from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
import shutil
from django.conf import settings


def user_directory_path(instance, filename):
    # Путь будет выглядеть как 'media/profile_images/username/filename'
    return f'media/profile_images/{instance.user.username}/{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

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

        if not self.profile_picture or self.profile_picture.name == 'default.jpg':
            # Путь к дефолтному изображению
            default_image_path = os.path.join(settings.STATIC_URL, 'media/default_images/profile_images/default.jpg')
            # Путь к директории для изображений пользователя
            user_image_path = os.path.join(settings.MEDIA_ROOT,
                                           f'profile_images/{self.user.username}/default.jpg')

            # Создаем директорию, если ее еще нет
            os.makedirs(os.path.dirname(user_image_path), exist_ok=True)

            # Копируем дефолтное изображение
            shutil.copy(default_image_path, user_image_path)
            # Обновляем ссылку на скопированное изображение
            self.profile_picture.name = f'profile_images/{self.user.username}/profile_picture.jpg'
            super().save(*args, **kwargs)  # Сохраняем изменения

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path, quality=90)
