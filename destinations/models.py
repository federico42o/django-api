from django.db import models


class Location(models.Model):
        name = models.CharField(max_length=30)
        latitude = models.DecimalField(max_digits=22, decimal_places=16)
        longitude = models.DecimalField(max_digits=22, decimal_places=16)
        country = models.CharField(max_length=30)

        def __str__(self):
            return self.name


class Destination(models.Model):
        name = models.CharField(max_length=30)
        description = models.CharField(max_length=255)
        information = models.CharField(max_length=255)
        location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name = 'destinations')

        def __str__(self):
            return self.name
        
