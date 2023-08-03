from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import City
from cities_light.models import Region
from cities_light.models import Country



class Location(models.Model):
    """Location Model"""
    
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE
    )
    region = ChainedForeignKey(
        Region, chained_field="country", chained_model_field="country"
    )
    city = ChainedForeignKey(
        City,
        chained_field="region",
        chained_model_field="region",
        null=True,
        blank=True,
    )
    zip = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.country}"
    
    class Meta:
        # pylint: disable=too-few-public-methods
        # pylint: disable=missing-class-docstring
        
        verbose_name = "location"
        verbose_name_plural = "locations"
