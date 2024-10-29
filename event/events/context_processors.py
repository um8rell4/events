from .models import UserProfile


def user_context(request):
    is_organizer = False
    if request.user.is_authenticated:
        # Проверяем, является ли пользователь организатором
        is_organizer = UserProfile.objects.filter(user=request.user, is_organizer=True).exists()
    return {
        'is_organizer': is_organizer
    }