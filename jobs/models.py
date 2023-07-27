from django.db import models
from cities_light.models import City
from cities_light.models import Region
from cities_light.models import Country
from users.models import User, Company, Skill
from smart_selects.db_fields import ChainedForeignKey


class JobType(models.Model):
    """Job Type Model"""

    name = models.CharField(max_length=255)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_type"
        verbose_name = "job type"
        verbose_name_plural = "job types"


class JobPost(models.Model):
    """Job Post-Model"""

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    job_description = models.TextField()
    job_location = models.ForeignKey("JobLocation", on_delete=models.CASCADE)
    job_category = models.ForeignKey("JobCategory", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    min_required_experience = models.IntegerField()
    max_required_experience = models.IntegerField()
    is_no_work_experience = models.BooleanField(default=True)
    job_seeker_level = models.CharField(max_length=255)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_post"
        verbose_name = "job post"
        verbose_name_plural = "job posts"


class JobLocation(models.Model):
    """Job Location Model"""

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = ChainedForeignKey(
        Region, chained_field="country", chained_model_field="country"
    )
    city = ChainedForeignKey(
        City, chained_field="country", chained_model_field="country"
    )
    zip = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_location"
        verbose_name = "job location"
        verbose_name_plural = "job locations"


class JobActivity(models.Model):
    """Job Post-Activity Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    apply_date = models.DateTimeField()

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_post_activity"
        verbose_name = "job activity"
        verbose_name_plural = "job activities"


class JobSkill(models.Model):
    """Job Post-Skill Model"""

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    skill_level = models.IntegerField()

    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring

        db_table = "job_post_skill"
        verbose_name = "job skill"
        verbose_name_plural = "job skills"


class JobCategory(models.Model):
    """Job Category Model"""
    name = models.CharField(max_length=255)
    description = models.TextField()
