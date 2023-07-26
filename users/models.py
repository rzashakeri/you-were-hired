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


class SeekerProfile(models.Model):
    """Job Seeker Profile Model"""

    # pylint: disable=too-few-public-methods
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_salary = models.IntegerField()
    is_annually_monthly = models.BooleanField(default=False)
    currency = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "seeker"
        verbose_name = "seeker"
        verbose_name_plural = "seekers"


class SeekerSkill(models.Model):
    """JobSeeker Skill Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)
    skill_level = models.IntegerField()

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "seeker_skill"
        verbose_name = "seeker_skill"
        verbose_name_plural = "seeker_skills"


class Skill(models.Model):
    """Skill Model"""

    skill_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "skill"
        verbose_name = "skill"
        verbose_name_plural = "skills"


class EducationDetail(models.Model):
    """Education Detail Model"""

    # pylint: disable=too-few-public-methods
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
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
    image = models.ImageField(upload_to='company/')
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "company_image"
        verbose_name = "company image"
        verbose_name_plural = "company images"
