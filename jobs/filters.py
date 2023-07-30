import django_filters
from django.forms import SelectMultiple
from django import forms
from jobs.models import Job
from utils.choices import JOB_TYPE_CHOICES, LEVEL_CHOICES, EXPERIENCE_CHOICES


class JobFilter(django_filters.FilterSet):
    type = django_filters.MultipleChoiceFilter(
        choices=JOB_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
            }
        )
    )
    level = django_filters.MultipleChoiceFilter(
        choices=LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
            }
        )
    )
    experience = django_filters.MultipleChoiceFilter(
        choices=EXPERIENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
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
    
    class Meta:
        model = Job
        fields = ["type", "level", "experience"]
