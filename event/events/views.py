from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from .models import Event, Booking
from .forms import EventForm
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


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
    print(request.user.is_anonymous)
    if request.user.is_anonymous:
        unregistered = True
        return render(request, 'events/event_detail.html', {'unregistered': unregistered, 'event': event})
    unregistered_person = Booking.objects.filter(user=request.user, event=event).exists()
    return render(request, 'events/event_detail.html', {'event': event, 'unregistered_person': unregistered_person})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            event.organizer = user_profile
            event.save()
            return redirect(to='events:events')
        else:
            print(form.errors)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {"form": form})


def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.organizer.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete")

    if request.method == 'POST':
        event.delete()
        return redirect('events:events')

    return render(request, 'events/event_delete.html', {'event': event})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.organizer.user != request.user:
        return redirect(to='events:toggle_booking', pk=pk)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            print(form.errors)
            return redirect('events:toggle_booking', pk=pk)
    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_edit.html', {'form': form, 'event': event})


@login_required
def toggle_booking(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user == event.organizer.user:
        return HttpResponseForbidden("You are can not register to this event")

    user_booking_exists = Booking.objects.filter(user=request.user, event=event).exists()

    if request.method == "POST":
        if user_booking_exists:
            Booking.objects.filter(user=request.user, event=event).delete()
        else:
            Booking.objects.create(user=request.user, event=event, status="Registered")
        return redirect(event.get_absolute_url())

    return render(request, "events/toggle_booking.html",
                  {"event": event, "user_booking_exists": user_booking_exists}
                  )

#Получить записи брони для данного ивента

#Записаться может только авторизованный пользователь
#Организатор не может записаться
#Записаться один и тот же пользователь дважды не может
