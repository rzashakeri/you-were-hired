from django.contrib import admin

from jobs.models import Job


@admin.register(Job)
class EducationDetailAdmin(admin.ModelAdmin):
    pass


