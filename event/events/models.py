from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=40, verbose_name='Название ивента')
    description = models.TextField(max_length=1000, verbose_name='Описание ивентов')
    location = models.CharField(max_length=100, verbose_name='Расположение')
    date = models.DateField(auto_now=False, verbose_name='Дата проведения')
    time = models.TimeField(verbose_name='Время проведения')
    max_participants = models.IntegerField(verbose_name='Максимальное количество участников')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Удаленный пользователь')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-status']

    def __str__(self):
        return self.status
