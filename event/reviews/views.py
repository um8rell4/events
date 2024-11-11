from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Event
from events.models import Booking
from users.models import UserProfile
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def event_reviews(request, pk):
    # Получаем мероприятие по первичному ключу (pk)
    event = get_object_or_404(Event, pk=pk)
    # Оптимизируем запрос с использованием select_related для извлечения User
    reviews = Review.objects.filter(event=event, is_published=True)

    access = False  # Изначально доступ закрыт

    if request.user.is_authenticated:
        # Проверяем, оставил ли пользователь комментарий на этом мероприятии
        user_comment_count = Review.objects.filter(user=request.user, event=event).count()

        # Проверяем, забронировал ли пользователь участие в этом мероприятии
        booking_user = Booking.objects.filter(user=request.user, event=event).exists()

        # Даем доступ для добавления комментария, если он не организатор
        access = booking_user and request.user != event.organizer

        if request.method == 'POST':
            form = ReviewForm(request.POST)

            # Проверка на наличие комментария
            if user_comment_count >= 1:
                return redirect('reviews:denied', pk=pk)

            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user  # Сохраняем текущего пользователя
                review.event = event
                review.save()
                return redirect('reviews:event_review', pk=pk)
            else:
                print(form.errors)
        else:
            form = ReviewForm()
    else:
        form = None  # Если пользователь не аутентифицирован, формы нет

    return render(
        request,
        'review/review_detail.html',
        {
            'event': event,
            'reviews': reviews,
            'form': form,
            'access': access,
            'user_delete_comment_access': user_comment_count > 0 if request.user.is_authenticated else False,
        }
    )


@login_required
def review_comment_delete(request, pk, comment_pk):

    # получаем текущий коммент
    comment = get_object_or_404(Review, pk=comment_pk)

    # получаем событие для возврата на страницу
    event = get_object_or_404(Event, pk=pk)

    # является ли авторизованный пользователь автором коммента
    if comment.user == request.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('reviews:event_review', pk=pk)
    # Если пользователь не является автором, возвращаем его обратно на страницу
    else:
        return redirect('reviews:event_review', pk=pk)

    return render(request, 'review/review_comment_delete.html', {'event': event})


@login_required
def reviews_comment_denied(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'review/review_denied.html', {'event': event})


def reviews(request):
    events_reviews = Review.objects.filter(is_published=True)
    return render(request, 'review/reviews.html', {'reviews': events_reviews})


@login_required
def review_delete(request, pk, comment_id):

    event = get_object_or_404(Event, pk=pk)  # Указываем модель Event
    comment = get_object_or_404(Review, id=comment_id)

    if request.method == 'POST':
        comment.delete()
        # Редирект на страницу отзывов этого события
        return redirect('reviews:event_review', pk=event.pk)

    return render(request, 'review/review_delete.html', {
        'event': event,
        'comment': comment
    })
# Create your views here.
