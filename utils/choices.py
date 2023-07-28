from django.utils.translation import gettext_lazy as _

# db constants =>
GENDER_CHOICES = (
    ("male", _("Male")),
    ("female", _("Female")),
    ("not specified", _("Not Specified")),
)

LEVEL_CHOICES = (
    ("senior", _("Senior")),
    ("mid-Level", _("Mid-Level")),
    ("junior", _("Junior")),
    ("intern", _("Intern")),
    ("not specified", _("Not Specified")),
)

STATUS_CHOICES = (
    ("pending", _("Pending")),
    ("seen", _("Seen")),
    ("accepted", _("Accepted")),
)

EXPERIENCE_CHOICES = (
    ("Under 1 Year", _("Under 1 Year")),
    ("1 - 2 Year", _("1 - 2 Year")),
    ("3 - 4 Year", _("3 - 4 Year")),
    ("5 - 6 Year", _("5 - 6 Year")),
    ("Over 6 years", _("Over 6 years")),
    ("No Experience", _("No Experience")),
)

JOB_TYPE_CHOICES = (
    ("Full Time Jobs", _("Full Time Jobs")),
    ("Part Time Jobs", _("Part Time Jobs")),
    ("Contract Jobs", _("Contract Jobs")),
    ("Remote", _("Remote")),
)
