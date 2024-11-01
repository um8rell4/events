from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from .models import Event, Booking
from .forms import EventForm
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from reviews.models import Review
from django.db.models import Avg


def events(request):
    elements = Event.objects.all().annotate(avg_rating=Avg('review__rating'))
    return render(
        request,
        'events/events.html', {
            'elements': elements,
        }
    )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    organizer = get_object_or_404(User, username=event.organizer)
    organizer_profile = UserProfile.objects.get(user=organizer)
    rating = Review.objects.filter(event=event.pk).aggregate(Avg("rating", default=0))
    #Количество записанных на мероприятие человек

    registered_persons = Booking.objects.filter(event=event).count()
    if request.user.is_anonymous:
        return render(request, 'events/event_detail.html', {'event': event,
                                                            'rating': rating,
                                                            'registered_persons': registered_persons,
                                                            'organizer_profile': organizer_profile})
    unregistered_person = Booking.objects.filter(user=request.user, event=event).exists()
    return render(request, 'events/event_detail.html', {'event': event,
                                                        'unregistered_person': unregistered_person,
                                                        'registered_persons': registered_persons,
                                                        'rating': rating,
                                                        'organizer_profile': organizer_profile})


@login_required
def create_event(request):

    is_organizer = UserProfile.objects.filter(user=request.user, is_organizer=True).exists()

    if not is_organizer:
        return redirect(to='events:events')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect(to='events:events')
        else:
            print(form.errors)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {"form": form})


def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.organizer != request.user:
        return HttpResponseForbidden("You are not allowed to delete")

    if request.method == 'POST':
        event.delete()
        return redirect('events:events')

    return render(request, 'events/event_delete.html', {'event': event})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.organizer != request.user:
        return redirect(event.get_absolute_url())

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect(event.get_absolute_url())
    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_edit.html', {'form': form, 'event': event})


@login_required
def toggle_booking(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user == event.organizer:
        return HttpResponseForbidden("You are can not register to this event")

    user_booking_exists = Booking.objects.filter(user=request.user, event=event).exists()
    # Количество записанных на мероприятие человек
    registered_persons = Booking.objects.filter(event=event).count()

    if request.method == "POST":
        if user_booking_exists:
            Booking.objects.filter(user=request.user, event=event).delete()
        else:
            Booking.objects.create(user=request.user, event=event, status="Registered")
        return redirect(event.get_absolute_url())

    return render(request, "events/toggle_booking.html",
                  {"event": event, "user_booking_exists": user_booking_exists,
                   "registered_persons": registered_persons}
                  )

#Получить записи брони для данного ивента

#Записаться может только авторизованный пользователь
#Организатор не может записаться
#Записаться один и тот же пользователь дважды не может
