from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default="Удаленный пользователь",
        verbose_name='Пользователь'
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Rating")
    comment = models.TextField(max_length=1500, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-rating']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
