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
from smart_selects.db_fields import ChainedForeignKey
from djmoney.models.fields import MoneyField
from file_validator.models import ValidatedFileField
from multiselectfield import MultiSelectField
from multiselectfield.utils import get_max_length


class Job(models.Model):
    """Job Model"""

    type = MultiSelectField(
        choices=JOB_TYPE_CHOICES,
        max_choices=3,
        max_length=get_max_length(JOB_TYPE_CHOICES, None),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="job")
    created_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    job_description = models.TextField()
    job_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="job"
    )
    job_category = models.ForeignKey(
        "JobCategory", on_delete=models.CASCADE, related_name="job"
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
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job"
        verbose_name = "job"
        verbose_name_plural = "jobs"


class JobActivity(models.Model):
    """Job Activity Model"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_activity"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_activity")
    apply_date = models.DateTimeField()

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_activity"
        verbose_name = "job activity"
        verbose_name_plural = "job activities"


class JobCategory(models.Model):
    """Job Category Model"""

    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_category"
        verbose_name = "job category"
        verbose_name_plural = "job categories"


class JobRequest(models.Model):
    """Job Request Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
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

        db_table = "job_request"
        verbose_name = "job request"
        verbose_name_plural = "job requests"


class JobBookmark(models.Model):
    """Job Bookmark Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    bookmark_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_bookmark"
        verbose_name = "job bookmark"
        verbose_name_plural = "job bookmarks"
