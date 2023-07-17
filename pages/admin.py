"""admin section page"""
from django.contrib import admin

from pages.models import PageModel

admin.site.register(PageModel)
