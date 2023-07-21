"""pages url"""
from django.urls import path

from jobs.views import JobsView

urlpatterns = [path("", JobsView.as_view(), name="jobs")]
