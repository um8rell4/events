from django.urls import path, include
from .views import CustomLogin, SignupView, user_profile, user_profile_edit, delete_profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLogin.as_view(redirect_authenticated_user=True, template_name='registration/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>', user_profile, name='user_profile'),
    path('profile/edit/', user_profile_edit, name='user_profile_edit'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    path('organizer/', include(('organizers.urls', 'organizers'), namespace='organizers'))
]
