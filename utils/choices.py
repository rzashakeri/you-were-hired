from django.utils.translation import gettext_lazy as _

# db constants =>
GENDER_CHOICES = (
    ("male", _("Male")),
    ("female", _("Female")),
    ("no matter", _("No matter")),
)

LEVEL_CHOICES = (
    ("senior", _("Senior")),
    ("mid-Level", _("Mid-Level")),
    ("junior", _("Junior")),
    ("intern", _("Intern")),
    ("no matter", _("No matter")),
)

STATUS_CHOICES = (
    ("pending", _("Pending")),
    ("seen", _("Seen")),
    ("accepted", _("Accepted")),
)

EXPERIENCE_CHOICES = (
    ("under 3 years", _("Under 3 Year")),
    ("3 - 6 year", _("3 - 5 Year")),
    ("over 6 years", _("Over 6 years")),
    ("no matter", _("No matter")),
)

JOB_TYPE_CHOICES = (
    ("full time jobs", _("Full Time Jobs")),
    ("part time jobs", _("Part Time Jobs")),
    ("contract jobs", _("Contract Jobs")),
    ("remote", _("Remote")),
    ("no matter", _("No matter")),
)
