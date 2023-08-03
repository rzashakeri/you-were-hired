from django.contrib import admin
from users.models import (
    JobSeeker,
    Education,
    Experience, Skill, Social,
)


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    """Seeker Profile Admin"""
    
    list_display = ["__str__", "gender", "level", "location"]
    list_filter = ["gender", "level", "location"]


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
