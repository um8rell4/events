from django.shortcuts import render, get_object_or_404
from .models import Event


def index(request):
    return render(request, 'base.html')


def events(request):
    elements = Event.objects.all()
    color = 'red'
    return render(
        request,
        'events/events.html', {
            'elements': elements,
            'color': color
        }
    )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {
        'event': event
    })
