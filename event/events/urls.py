from django.urls import path
from .views import events, event_detail, create_event, delete_event, event_edit,toggle_booking


urlpatterns = [
    path('', events, name='events'),
    path('detail/<int:pk>/', event_detail, name='event_detail'),
    path('create/', create_event, name='create_event'),
    path('detail/<int:pk>/', delete_event, name='event_delete'),
    path('event/<int:pk>/delete/', delete_event, name='delete_event'),
    path('event/<int:pk>/edit/', event_edit, name='edit_event'),
    path('events/<int:event_id>/toggle_booking/', toggle_booking, name='toggle_booking'),
]
