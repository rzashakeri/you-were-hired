from django.contrib import admin

from jobs.models import Job, Category


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Job Admin"""
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    pass
