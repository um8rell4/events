from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=40, verbose_name='Название ивента')
    description = models.TextField(max_length=10000, verbose_name='Описание ивентa')
    location = models.CharField(max_length=100, verbose_name='Расположение')
    date = models.DateField(auto_now=False, verbose_name='Дата проведения')
    time = models.TimeField(verbose_name='Время проведения')
    max_participants = models.IntegerField(verbose_name='Максимальное количество участников')
    bg_image = models.ImageField(upload_to='event_images/', verbose_name='Картинка мероприятия',
                                 blank=True, null=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail', args=[
            self.pk
        ])


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-status']

    def __str__(self):
        return self.status
