from django.urls import path
from .views import organizer_panel, info_card, publish_review


urlpatterns = [
    path('', organizer_panel, name='index'),
    path('detail/<int:pk>', info_card, name='info_card'),
    path('detail/publish/<int:pk>', publish_review, name='publish'),
]
