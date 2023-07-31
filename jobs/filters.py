import django_filters
from django import forms
from jobs.models import Job
from utils.choices import JOB_TYPE_CHOICES, LEVEL_CHOICES, EXPERIENCE_CHOICES
from dal import autocomplete


class JobFilter(django_filters.FilterSet):
    TAILWIND_CLASS = "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
    
    # This section for search =>
    job_title = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name="title",
    )
    job_location = django_filters.CharFilter(field_name="location__region__name", lookup_expr='icontains')
    job_type = django_filters.CharFilter(field_name="type", lookup_expr='icontains')
    job_experience = django_filters.CharFilter(field_name="experience", lookup_expr='icontains')
    
    # This section for filter =>
    type = django_filters.MultipleChoiceFilter(
        choices=JOB_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        )
    )
    level = django_filters.MultipleChoiceFilter(
        choices=LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        )
    )
    experience = django_filters.MultipleChoiceFilter(
        choices=EXPERIENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        )
    )
    order_by = django_filters.OrderingFilter(
        choices=(
            ('created_date', 'Newest'),
            ('-salary', 'Most Salary'),
        ),
        empty_label=None
    )

