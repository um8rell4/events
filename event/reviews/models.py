from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from users.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):

    RATING_CHOICES = [
        (5, "5 - Отлично"),
        (4, "4 - Хорошо"),
        (3, "3 - Неплохо"),
        (2, "2 - Плохо"),
        (1, "1 - Очень плохо"),
    ]

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_DEFAULT,
        default="Удаленный пользователь",
        verbose_name='Пользователь'
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    rating = models.FloatField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)],
                               verbose_name="Rating")
    comment = models.TextField(max_length=1500, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-rating']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
