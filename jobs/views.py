from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.gis.geoip2 import GeoIP2
from ipware import get_client_ip
from django.conf import settings

from jobs.filters import JobFilter
from jobs.models import Job


class JobsView(View):
    """Job View"""
    
    def get(self, request):
        # pylint: disable=missing-docstring
        if settings.DEBUG:
            # We are in debug mode, so we set it to a dummy value.
            client_ip = "8.8.8.8"
        else:
            client_ip, is_routable = get_client_ip(request)
            if client_ip is None:
                pass
            else:
                if is_routable:
                    pass
                else:
                    pass
        
        geo_ip = GeoIP2()
        country = geo_ip.country(client_ip)["country_name"]
        jobs = JobFilter(
            request.GET,
            queryset=Job.objects.filter(
                location__country__name__contains=country
            ).all(),
        )
        context = {"jobs": jobs}
        return render(request, "jobs/jobs.html", context)
