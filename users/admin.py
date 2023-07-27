from django.contrib import admin

from users.models import UserType, User


class UserAdmin(admin.ModelAdmin):
    """User Model Admin"""
    list_display = ["username", "first_name", "last_name", "user_type", "is_staff", "is_superuser"]
    list_filter = ["is_staff", "is_superuser", "user_type"]


admin.site.register(User, UserAdmin)
