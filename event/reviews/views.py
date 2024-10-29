from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Event
from events.models import Booking
from users.models import UserProfile
from .forms import ReviewForm


def event_reviews(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event_review = Review.objects.filter(event=event)
    if not request.user.is_anonymous:
        booking_user = Booking.objects.filter(user=request.user, event=event).exists()
        access = booking_user and request.user != event.organizer
    else:
        access = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            review.user = user_profile
            review.event = Event.objects.get(pk=pk)
            review.save()
            return redirect('reviews:event_review', pk=pk)
        else:
            print(form.errors)
    else:
        form = ReviewForm()

    return render(request, 'review/review_detail.html', {'event': event,
                                                         'event_review': event_review,
                                                         'form': form,
                                                         'access': access})


def reviews(request):
    events_reviews = Review.objects.all()
    return render(request, 'review/reviews.html', {'reviews': events_reviews})
# Create your views here.
