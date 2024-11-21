from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import User, UserProfile
from reviews.models import Review
from events.models import Event, Booking
from .forms import EventOrganizerForm


@login_required
def organizer_panel(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'organizers/organizer_panel.html', {"events": events})


@login_required
def info_card(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reviews = Review.objects.filter(event=event)
    if event.organizer == request.user:
        if request.method == 'POST':
            form = EventOrganizerForm(request.POST)
            if form.is_valid():
                organizer_form = form.save(commit=False)
                organizer_form.event_id = pk
                organizer_form.save()
                return redirect(to='users:organizers:info_card', pk=pk)
            else:
                print(form.errors)
        else:
            form = EventOrganizerForm
        return render(request, 'organizers/organizer_event_edit.html', {"event": event, "reviews": reviews,
                                                                        "form": form})
    else:
        return redirect(to='events:events')


@login_required
def publish_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.is_published = True
        review.save()
    return redirect('users:organizers:info_card', pk=review.event.pk)


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
    return redirect('users:organizers:info_card', pk=review.event.pk)

