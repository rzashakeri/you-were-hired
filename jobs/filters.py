import django_filters
from django.forms import SelectMultiple
from django import forms
from jobs.models import Job, Type, Level, Experience, Salary


class JobFilter(django_filters.FilterSet):
    type = django_filters.ModelMultipleChoiceFilter(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
            }
        ),
    )
    level = django_filters.ModelMultipleChoiceFilter(
        queryset=Level.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
            }
        )
    )
    experience = django_filters.ModelMultipleChoiceFilter(
        queryset=Experience.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:border-gray-600"
            }
        )
    )

    class Meta:
        model = Job
        fields = ["type", "level", "experience"]
