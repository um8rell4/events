from django.urls import path
from .views import events, event_detail


urlpatterns = [
    path('', events, name='events'),
    path('detail/<int:pk>/', event_detail, name='event_detail')
]
