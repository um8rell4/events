from django.urls import path, include
from .views import CustomLogin, SignupView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLogin.as_view(redirect_authenticated_user=True, template_name='registration/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
