from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Event
from users.models import UserProfile
from .forms import ReviewForm


def event_reviews(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reviews = Review.objects.filter(event=event)

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

    return render(request, 'review/review.html', {'event': event,
                                                  'reviews': reviews,
                                                  'form': form})
# Create your views here.
