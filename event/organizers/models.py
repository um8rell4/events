from django.db import models
from events.models import Event


class EventOrganizer(models.Model):

    STATUS_CHOICES = [
        (1, "Подготовка"),
        (2, "В процессе"),
        (3, "Завершен"),
        (4, "Отменен"),
    ]

    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    event_status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='Статус мероприятия', default=1)

    class Meta:
        verbose_name = 'Статус мероприятия'
        verbose_name_plural = 'Статусы мероприятий'

    def __str__(self):
        return self.event_status
# Create your models here.
