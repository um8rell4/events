from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', event_reviews, name='event_review'),
    path('', reviews, name='reviews'),
    path('<int:pk>/denied', reviews_comment_denied, name='denied'),
    path('<int:pk>/delete/<int:comment_pk>/', review_comment_delete, name='review_delete'),
]
