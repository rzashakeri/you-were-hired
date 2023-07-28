from django.contrib import admin
from users.models import (
    JobSeeker,
    Skill,
    Education,
    Experience,
    Company, Location, Social,
)


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    """Seeker Profile Admin"""
    
    list_display = ["__str__", "gender", "level", "location"]
    list_filter = ["gender", "level", "location"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Seeker Skill Admin"""
    
    list_display = ["name", "level"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Education Detail Admin"""
    
    list_display = ["profile"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Experience Detail Admin"""
    
    list_display = ["profile", "job_title", "company_name"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Experience Detail Admin"""
    
    list_display = ["user", "name", "website_url", "is_verified"]


@admin.register(Location)
class CompanyAdmin(admin.ModelAdmin):
    """Company Admin"""
    pass


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    """Company Admin"""
    pass
