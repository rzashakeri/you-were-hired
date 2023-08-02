"""pages url"""
from django.urls import path

from jobs.views import JobsView, JobView

urlpatterns = [
    path("", JobsView.as_view(), name="jobs"),
    path("<slug:company>/<slug:slug>/<int:id>/", JobView.as_view(), name='job')
]
