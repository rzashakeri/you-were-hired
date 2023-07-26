from django.db import models

from users.models import User


class JobType(models.Model):
    """Job Type Model"""
    name = models.CharField(max_length=255)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        db_table = "job_type"
        verbose_name = "job type"
        verbose_name_plural = "job types"
