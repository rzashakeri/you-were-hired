from django.contrib import admin

from utils.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Company Admin"""
    pass

