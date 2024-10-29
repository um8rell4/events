from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', event_reviews, name='event_review'),
    path('', reviews, name='reviews')
]
