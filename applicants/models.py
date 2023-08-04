from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User
from utils.choices import LEVEL_CHOICES, GENDER_CHOICES
from birthday import BirthdayField, BirthdayManager
from djmoney.models.fields import MoneyField
from file_validator.models import ValidatedFileField


class Applicant(models.Model):
    """Applicant Model"""
    # pylint: disable=too-few-public-methods
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to="user/profile/images/",
        null=True,
        blank=True,
    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=13,
        choices=GENDER_CHOICES,
        default="not specified",
        null=True,
        blank=True,
    )
    last_apply_job_date = models.DateTimeField(null=True, blank=True)
    birthday = BirthdayField(null=True, blank=True)
    birthday_objects = BirthdayManager()
    current_salary = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", null=True, blank=True
    )
    is_annually_monthly = models.BooleanField(default=False)
    level = models.CharField(
        max_length=13,
        choices=LEVEL_CHOICES,
        default="not specified",
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "job seeker"
        verbose_name_plural = "job seekers"


class Education(models.Model):
    """Education Model"""
    
    # pylint: disable=too-few-public-methods
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="educations"
    )
    certificate_degree_name = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    institute_university_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    cgpa = models.IntegerField(null=True, blank=True)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "education"
        verbose_name_plural = "educations"


class Experience(models.Model):
    """Experience Model"""
    
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="experiences"
    )
    is_current_job = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    job_location_city = models.CharField(max_length=255, null=True, blank=True)
    job_location_state = models.CharField(max_length=255, null=True, blank=True)
    job_location_country = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "experience"
        verbose_name_plural = "experiences"


class Skill(models.Model):
    """Skill Model"""
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="skills"
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default=1
    )
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "skill"
        verbose_name_plural = "skills"


class Social(models.Model):
    """Social Model"""
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="social_accounts"
    )
    name = models.CharField(max_length=100)
    url = models.URLField()
    
    def __str__(self):
        return str(self.name)
