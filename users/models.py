from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from django.contrib.auth.models import User
from utils.choices import LEVEL_CHOICES, GENDER_CHOICES
from birthday import BirthdayField, BirthdayManager
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from file_validator.models import ValidatedFileField
from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import City
from cities_light.models import Region
from cities_light.models import Country


class JobSeeker(models.Model):
    """JobSeeker Model"""
    
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
    phone = PhoneNumberField(null=True, blank=True)
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
    skill = models.ForeignKey(
        "Skill",
        on_delete=models.CASCADE,
        related_name="job_seekers",
        null=True,
        blank=True,
    )
    location = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE,
        related_name="job_seekers",
        null=True,
        blank=True,
    )
    social = models.ForeignKey(
        "Social",
        on_delete=models.CASCADE,
        related_name="job_seekers",
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        db_table = "job_seeker"
        verbose_name = "job seeker"
        verbose_name_plural = "job seekers"


class Skill(models.Model):
    """Skill Model"""
    
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


class Education(models.Model):
    """Education Model"""
    
    # pylint: disable=too-few-public-methods
    profile = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="educations")
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
    
    profile = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="experiences")
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


class Location(models.Model):
    """Location Model"""
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="locations")
    region = ChainedForeignKey(
        Region, chained_field="country", chained_model_field="country"
    )
    city = ChainedForeignKey(
        City, chained_field="region", chained_model_field="region", null=True, blank=True
    )
    zip = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.country} | {self.region}"
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "location"
        verbose_name_plural = "locations"


class Social(models.Model):
    """Social Model"""
    
    name = models.CharField(max_length=100)
    url = models.URLField()


class Company(models.Model):
    """Company Model"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    logo = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to="company/logo/images/",
        null=True,
        blank=True,
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="companies")
    establishment_date = models.DateTimeField()
    website_url = models.URLField()
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    size = models.CharField(max_length=50)
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name="companies")
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        verbose_name = "company"
        verbose_name_plural = "companies"


class CompanyImage(models.Model):
    """Company Image Model"""
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_images")
    image = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to="company/images/",
        null=True,
        blank=True,
    )
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "company image"
        verbose_name_plural = "company images"
