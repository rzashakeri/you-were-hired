from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from cities_light.models import City
from cities_light.models import Region
from cities_light.models import Country
from django.urls import reverse
from django_extensions.db.fields import ShortUUIDField

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
from ckeditor.fields import RichTextField
import django_filters


class Job(models.Model):
    """Job Model"""
    
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    created_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    description = RichTextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="jobs")
    category = models.ManyToManyField("Category")
    is_active = models.BooleanField(default=True)
    type = models.CharField(
        max_length=14,
        choices=JOB_TYPE_CHOICES,
        default="No matter",
    )
    level = models.CharField(
        max_length=9,
        choices=LEVEL_CHOICES,
        default="No matter",
    )
    experience = models.CharField(
        max_length=13,
        choices=EXPERIENCE_CHOICES,
        default="No matter",
    )
    salary = MoneyField(
        max_digits=14, decimal_places=0, default_currency="USD", null=True, blank=True
    )
    skill = models.ManyToManyField(Skill)
    slug = AutoSlugField(populate_from="title")
    

    def __str__(self):
        return f"{self.title} | {self.company}"
    
    def get_absolute_url(self):
        return reverse('job', kwargs={'id': self.pk, 'slug': self.slug, 'company': self.company.slug})

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Job, self).save(*args, **kwargs)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        db_table = "job"
        verbose_name = "job"
        verbose_name_plural = "jobs"


class Activity(models.Model):
    """Job Activity Model"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="activities")
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
