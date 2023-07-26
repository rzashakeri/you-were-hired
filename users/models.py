from django.db import models
from django.contrib.auth.models import AbstractUser
from birthday import BirthdayField, BirthdayManager
from phone_field import PhoneField
from djmoney.models.fields import MoneyField


class UserType(models.Model):
    """This Model To determine the user is a job-seeker or a recruiter"""

    # pylint: disable=too-few-public-methods

    user_type_name = models.CharField(max_length=100)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        db_table = "user_type"
        verbose_name = "user type"
        verbose_name_plural = "user types"


class User(AbstractUser):
    """User Model"""

    # pylint: disable=too-few-public-methods

    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to="user/profile/", null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    birthday = BirthdayField(null=True, blank=True)
    birthday_objects = BirthdayManager()
    gender = None
    phone = PhoneField(null=True, blank=True, help_text="Contact phone number")
    sms_notification_active = models.BooleanField(default=False)
    email_notification_active = models.BooleanField(default=False)
    last_apply_job_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"


class JobSeekerProfile(models.Model):
    """Job Seeker Profile Model"""

    # pylint: disable=too-few-public-methods
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_salary = models.IntegerField()
    is_annually_monthly = models.BooleanField(default=False)
    currency = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")

