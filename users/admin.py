from django.contrib import admin
from users.models import (
    Profile,
    Education,
    Experience, Skill, Social,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Seeker Profile Admin"""

    list_display = ["user", "gender", "level"]
    list_filter = ["gender", "level"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Education Detail Admin"""

    list_display = ["profile"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Experience Detail Admin"""

    list_display = ["profile", "job_title", "company_name"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Seeker Skill Admin"""

    list_display = ["name", "level"]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    """Company Admin"""
    pass
