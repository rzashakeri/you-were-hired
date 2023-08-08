"""users url"""
from django.urls import path

from users.views import ProfileView

urlpatterns = [
    path('profile/<str:username>/', ProfileView.as_view(), name='profile')
]
