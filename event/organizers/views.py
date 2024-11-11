from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import User, UserProfile
from reviews.models import Review
from events.models import Event, Booking


@login_required
def organizer_panel(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'organizers/organizer_panel.html', {"events": events})


@login_required
def info_card(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reviews = Review.objects.filter(event=event)
    if event.organizer == request.user:
        return render(request, 'organizers/organizer_event_edit.html', {"event": event, "reviews": reviews})
    else:
        return redirect(to='events:events')


@login_required
def publish_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.is_published = True
        review.save()
    return redirect('users:organizers:info_card', pk=review.event.pk)
