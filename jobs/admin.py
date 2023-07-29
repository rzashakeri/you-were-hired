from django.contrib import admin

from jobs.models import Job, Category, Level, Salary, Experience, Type


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Job Admin"""
    list_display = ["title", "company", "created_date", "location", "salary"]
    list_filter = ["level", "experience", "level"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    pass


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    """Level Admin"""
    pass


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    """Salary Admin"""
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Salary Admin"""
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Salary Admin"""
    pass
