from django.urls import path
from .views import *


urlpatterns = [
    path('', events, name='events'),
    path('detail/<int:pk>/', event_detail, name='event_detail'),
    path('create/', create_event, name='create_event'),
    path('detail/<int:pk>/', delete_event, name='event_delete'),
    path('event/<int:pk>/delete/', delete_event, name='delete_event'),
    path('event/<int:pk>/edit/', event_edit, name='edit_event'),
    path('event/<int:pk>/toggle_booking/', toggle_booking, name='toggle_booking')
]
