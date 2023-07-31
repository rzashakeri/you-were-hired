import django_filters
from django import forms
from jobs.models import Job
from utils.choices import JOB_TYPE_CHOICES, LEVEL_CHOICES, EXPERIENCE_CHOICES
from dal import autocomplete


class JobFilter(django_filters.FilterSet):
    TAILWIND_CLASS = "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
    
    # This section for search =>
    title_search = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name="title",
    )
    location_search = django_filters.CharFilter(field_name="location__region__name", lookup_expr='icontains')
    type_search = django_filters.CharFilter(field_name="type", lookup_expr='icontains')
    experience_search = django_filters.CharFilter(field_name="experience", lookup_expr='icontains')
    
    # This section for filter =>
    type_filter = django_filters.MultipleChoiceFilter(
        choices=JOB_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="type",
        lookup_expr='icontains'
    )
    level_filter = django_filters.MultipleChoiceFilter(
        choices=LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="level",
        lookup_expr='icontains'
    )
    experience_filter = django_filters.MultipleChoiceFilter(
        choices=EXPERIENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="experience",
        lookup_expr='icontains'
    )
    
    # This filter shows in mobile breakpoints =>
    type = django_filters.ChoiceFilter(
        choices=JOB_TYPE_CHOICES,
        field_name="type",
        lookup_expr='icontains',
        empty_label=None
    )
    level = django_filters.ChoiceFilter(
        choices=LEVEL_CHOICES,
        field_name="level",
        lookup_expr='icontains',
        empty_label=None
    )
    experience = django_filters.ChoiceFilter(
        choices=EXPERIENCE_CHOICES,
        field_name="experience",
        lookup_expr='icontains',
        empty_label=None
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
        fields = ['type']