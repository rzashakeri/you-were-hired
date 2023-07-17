"""
pages app model
"""
from django.db import models


class PageModel(models.Model):
    """Page Model"""

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return str(self.name)
