"""Users View"""
from django.shortcuts import get_object_or_404, render
from django.views import View

from users.models import Profile


class ProfileView(View):
    """Home View"""
    
    def get(self, request, username):
        # pylint: disable=missing-docstring
        profile = get_object_or_404(Profile, user__username__iexact=username)
        context = {
            'profile': profile
        }
        return render(request, "users/profile.html", context)
