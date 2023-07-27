from django.contrib import admin
from users.models import UserType, User, SeekerProfile, SeekerSkill


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User Admin"""
    list_display = ["username", "first_name", "last_name", "gender", "user_type", "is_staff", "is_superuser"]
    list_filter = ["is_staff", "is_superuser", "user_type"]
    search_fields = ["first_name", "last_name", "username"]


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    """User Type Admin"""
    pass


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    """Seeker Profile Admin"""
    list_display = ["__str__", "birthday", "current_salary"]


@admin.register(SeekerSkill)
class SeekerSkillAdmin(admin.ModelAdmin):
    """Seeker Skill Admin"""
    list_display = ["profile", "skill"]
