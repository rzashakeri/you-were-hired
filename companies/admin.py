from django.contrib import admin

from companies.models import Company, Social


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Experience Detail Admin"""
    
    list_display = ["user", "name", "website_url", "is_verified"]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    """Company Admin"""
    pass
