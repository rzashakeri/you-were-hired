from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from cities_light.models import City
from cities_light.models import Region
from cities_light.models import Country

from users.models import Company, Skill, Location
from utils.choices import (
    STATUS_CHOICES,
    JOB_TYPE_CHOICES,
    LEVEL_CHOICES,
    EXPERIENCE_CHOICES,
)
from djmoney.models.fields import MoneyField
from file_validator.models import ValidatedFileField
from multiselectfield import MultiSelectField
from multiselectfield.utils import get_max_length
from autoslug import AutoSlugField


class Job(models.Model):
    """Job Model"""
    title = models.CharField(max_length=100)
    type = MultiSelectField(
        choices=JOB_TYPE_CHOICES,
        max_choices=3,
        max_length=get_max_length(JOB_TYPE_CHOICES, None),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    created_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=datetime.now() + timedelta(days=30), null=True, blank=True)
    description = models.TextField()
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="jobs"
    )
    category = models.ManyToManyField(
        "Category",
    )
    is_active = models.BooleanField(default=True)
    level = MultiSelectField(
        choices=LEVEL_CHOICES,
        max_choices=3,
        max_length=get_max_length(LEVEL_CHOICES, None),
    )
    experience = MultiSelectField(
        choices=EXPERIENCE_CHOICES,
        max_choices=3,
        max_length=get_max_length(EXPERIENCE_CHOICES, None),
    )
    salary = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", null=True, blank=True
    )
    skill = models.ManyToManyField(Skill)
    slug = AutoSlugField(populate_from='title')
    
    def __str__(self):
        return f"{self.title} | {self.company}"
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        db_table = "job"
        verbose_name = "job"
        verbose_name_plural = "jobs"


class Activity(models.Model):
    """Job Activity Model"""
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_activities"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_activities")
    apply_date = models.DateTimeField()
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "job activity"
        verbose_name_plural = "job activities"


class Category(models.Model):
    """Job Category Model"""
    
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "job category"
        verbose_name_plural = "job categories"


class Request(models.Model):
    """Job Request Model"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="requests")
    request_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()
    resume = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["application/pdf"],
        max_upload_file_size=10485760,
        upload_to="company/resume/",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="pending")
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "job request"
        verbose_name_plural = "job requests"


class Bookmark(models.Model):
    """Job Bookmark Model"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="bookmarks")
    bookmark_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "job bookmark"
        verbose_name_plural = "job bookmarks"
