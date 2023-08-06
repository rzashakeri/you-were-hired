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

COMPANY_SIZE_CHOICES = (
    ("under 10 people", _("Under 10 People")),
    ("11 to 50 people", _("11 To 50 People")),
    ("51 to 200 people", _("51 To 200 People")),
    ("201 to 500 people", _("201 To 500 People")),
    ("501 to 1000 people", _("501 To 1000 People")),
    ("1001 to 5000 people", _("1001 To 5000 People")),
    ("more than 5000 people", _("mMore Than 5000 People")),
)

ROLES_CHOICES = (
    ("applicant", _("applicant")),
    ("employer", _("employer")),
)

MARITAL_CHOICES = (
    ("married", _("Married")),
    ("single", _("Single")),
)
