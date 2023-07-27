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
    (0, _("Under 1 Year")),
    (1, _("1 - 2 Year")),
    (2, _("3 - 4 Year")),
    (3, _("5 - 6 Year")),
    (4, _("Over 6 years")),
    (5, _("No Experience")),
)

JOB_TYPE_CHOICES = (
    (0, _("Full Time Jobs")),
    (1, _("Part Time Jobs")),
    (2, _("Contract Jobs")),
    (3, _("Remote")),
)
