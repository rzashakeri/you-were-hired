from django.shortcuts import render
from django.views import View


class JobsView(View):
	def get(self, request):
		return render(request, "jobs/jobs.html")
