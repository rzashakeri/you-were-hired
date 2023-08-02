import django_filters
from django import forms
from django_filters.widgets import SuffixedMultiWidget

from jobs.models import Job, Category
from utils.choices import JOB_TYPE_CHOICES, LEVEL_CHOICES, EXPERIENCE_CHOICES
from dal import autocomplete


class RangeWidget(SuffixedMultiWidget):
    suffixes = ['min', 'max']
    
    def __init__(self, attrs=None, attrs_min=None, attrs_max=None):
        widgets = (
            forms.TextInput(attrs_min),
            forms.TextInput(attrs_max),
        )
        super(RangeWidget, self).__init__(widgets, attrs)
    
    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]
    
    def format_output(self, rendered_widgets):
        return '-'.join(rendered_widgets)


class JobFilter(django_filters.FilterSet):
    TAILWIND_CLASS = "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
    
    # This section for search =>
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name="title",
    )
    location = django_filters.CharFilter(field_name="location__region__name", lookup_expr='icontains')
    job_type = django_filters.CharFilter(field_name="type", lookup_expr='icontains')
    work_experience = django_filters.CharFilter(field_name="experience", lookup_expr='icontains')
    
    # This section for filter =>
    type = django_filters.MultipleChoiceFilter(
        choices=JOB_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="type",
        lookup_expr='icontains',
        label="Type"
    )
    level = django_filters.MultipleChoiceFilter(
        choices=LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="level",
        lookup_expr='icontains',
        label="Level"
    
    )
    experience = django_filters.MultipleChoiceFilter(
        choices=EXPERIENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="experience",
        lookup_expr='icontains',
        label="Experience"
    )
    category = django_filters.ModelMultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": TAILWIND_CLASS
            }
        ),
        field_name="category__name",
        lookup_expr='icontains',
        queryset=Category.objects.all(),
        label="Category"
    )
    
    salary = django_filters.RangeFilter(
        field_name="salary",
        lookup_expr='icontains',
        label="Salary",
        widget=RangeWidget(
            attrs_min={'placeholder': 'Min Salary'},
            attrs_max={'placeholder': 'Max Salary'},
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
        fields = ['type', 'category']
