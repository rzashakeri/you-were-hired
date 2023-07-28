from django.utils.translation import gettext_lazy as _

# db constants =>
GENDER_CHOICES = (
    ("Male", _("Male")),
    ("Female", _("Female")),
    ("Not Specified", _("Not Specified")),
)

LEVEL_CHOICES = (
    ("Senior", _("Senior")),
    ("Mid-Level", _("Mid-Level")),
    ("Junior", _("Junior")),
    ("Intern", _("Intern")),
    ("Not Specified", _("Not Specified")),
)

STATUS_CHOICES = (
    ("Pending", _("Pending")),
    ("Seen", _("Seen")),
    ("Accepted", _("Accepted")),
)

EXPERIENCE_CHOICES = (
    ("Under 1 Year", _("Under 1 Year")),
    ("1 - 2 Year", _("1 - 2 Year")),
    ("3 - 4 Year", _("3 - 4 Year")),
    ("5 - 6 Year", _("5 - 6 Year")),
    ("Over 6 Years", _("Over 6 years")),
    ("No Experience", _("No Experience")),
)

JOB_TYPE_CHOICES = (
    ("Full Time Jobs", _("Full Time Jobs")),
    ("Part Time Jobs", _("Part Time Jobs")),
    ("Contract Jobs", _("Contract Jobs")),
    ("Remote", _("Remote")),
)
