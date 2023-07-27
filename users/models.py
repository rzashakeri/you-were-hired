from django.core.validators import (
    MinValueValidator,
    MaxLengthValidator,
    MaxValueValidator,
)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from birthday import BirthdayField, BirthdayManager
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from file_validator.models import ValidatedFileField

GENDER_CHOICES = (
    (0, _("male")),
    (1, _("female")),
    (2, _("not specified")),
)

LEVEL_CHOICES = (
    (0, _("senior")),
    (1, _("mid-level")),
    (2, _("Junior")),
    (3, _("intern")),
    (4, _("not specified")),
)


class UserType(models.Model):
    """This Model To determine the user is a job-seeker or a recruiter"""

    # pylint: disable=too-few-public-methods

    user_type_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_type_name)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        db_table = "user_type"
        verbose_name = "user type"
        verbose_name_plural = "user types"


class User(AbstractUser):
    """User Model"""

    # pylint: disable=too-few-public-methods

    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)
    user_image = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to="user/profile/images/",
        null=True,
        blank=True,
    )
    full_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    phone = PhoneNumberField(null=True, blank=True)
    sms_notification_active = models.BooleanField(default=False)
    email_notification_active = models.BooleanField(default=False)
    last_apply_job_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"


class SeekerProfile(models.Model):
    """Job Seeker Profile Model"""

    # pylint: disable=too-few-public-methods
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = BirthdayField(null=True, blank=True)
    birthday_objects = BirthdayManager()
    current_salary = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    is_annually_monthly = models.BooleanField(default=False)
    currency = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    level = models.IntegerField(choices=LEVEL_CHOICES, default=4)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "seeker"
        verbose_name = "seeker"
        verbose_name_plural = "seekers"


class SeekerSkill(models.Model):
    """JobSeeker Skill Model"""

    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)
    skill_level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default=1
    )

    def __str__(self):
        return f"{self.profile.user.username} | {self.skill.skill_name}"

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "seeker_skill"
        verbose_name = "seeker skill"
        verbose_name_plural = "seeker skills"


class SeekerLevel(models.Model):
    """JobSeeker Level Model Such Senior | Mid-Level | Junior | Intern"""

    profile = models.OneToOneField(SeekerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "seeker_level"
        verbose_name = "seeker level"
        verbose_name_plural = "seeker levels"


class Skill(models.Model):
    """Skill Model"""

    skill_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.skill_name)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "skill"
        verbose_name = "skill"
        verbose_name_plural = "skills"


class EducationDetail(models.Model):
    """Education Detail Model"""

    # pylint: disable=too-few-public-methods
    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
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

        db_table = "education_detail"
        verbose_name = "education detail"
        verbose_name_plural = "education details"


class ExperienceDetail(models.Model):
    """Experience Detail Model"""

    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
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

        db_table = "experience_detail"
        verbose_name = "experience detail"
        verbose_name_plural = "experience details"


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
    )
    establishment_date = models.DateTimeField()
    company_website_url = models.URLField()

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "company"
        verbose_name = "company"
        verbose_name_plural = "companies"


class CompanyImage(models.Model):
    """Company Image Model"""

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=["image/png"],
        acceptable_types=["image"],
        max_upload_file_size=10485760,
        upload_to="company/images/",
    )

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "company_image"
        verbose_name = "company image"
        verbose_name_plural = "company images"
