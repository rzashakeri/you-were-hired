from django.db import models
from django.contrib.auth.models import User


class UsertypeModel(models.Model):
	"""This Model To determine the user is a job seeker or a recruiter"""
	
	user_type_name = models.CharField(max_length=100)
