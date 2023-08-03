from django.contrib import admin

from jobs.models import Job, Category, Skill


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Job Admin"""
    list_display = ["title", "company", "created_date", "location", "salary"]
    list_filter = ["level", "experience", "level", "type"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Seeker Skill Admin"""
    
    list_display = ["name", "level"]

