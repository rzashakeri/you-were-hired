from django.contrib import admin

from jobs.models import Job, Category


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "created_date", "location", "level", "experience"]
    list_filter = ["company", "created_date", "level", "experience"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


