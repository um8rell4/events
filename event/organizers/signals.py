from django.db.models.signals import post_save
from events.models import Event
from django.dispatch import receiver
from .models import EventOrganizer


@receiver(post_save, sender=Event)
def create_event(sender, instance, created, **kwargs):
    if created:
        EventOrganizer.objects.create(event=instance)


@receiver(post_save, sender=Event)
def save_event_status(sender, instance, **kwargs):
    instance.eventorganizer.save()
