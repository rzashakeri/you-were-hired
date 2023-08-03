from django.db import models
from django.contrib.auth.models import User
from utils import logo_directory_path
from phonenumber_field.modelfields import PhoneNumberField
from file_validator.models import ValidatedFileField
from autoslug import AutoSlugField

from utils.models import Location


class Company(models.Model):
    """Company Model"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    logo = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to=logo_directory_path,
        null=True,
        blank=True,
    )
    cover = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to="company/cover/images/",
        null=True,
        blank=True,
    )
    location = models.OneToOneField(
        Location, on_delete=models.CASCADE
    )
    establishment_date = models.DateTimeField()
    website_url = models.URLField()
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    size = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name")
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Company, self).save(*args, **kwargs)
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "company"
        verbose_name_plural = "companies"


class Image(models.Model):
    """Company Image Model"""
    
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_images"
    )
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


class Social(models.Model):
    """Social Model"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="social_accounts")
    name = models.CharField(max_length=100)
    url = models.URLField()
    
    def __str__(self):
        return str(self.name)
