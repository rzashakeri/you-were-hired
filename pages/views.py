"""Pages View"""
from django.shortcuts import render
from django.views import View


class HomeView(View):
    """Home View"""

    def get(self, request):
        return render(request, "pages/home.html")
