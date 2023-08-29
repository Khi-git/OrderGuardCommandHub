from django.contrib.gis.db import models

class MapLayer(models.Model):
    name = models.CharField(max_length=255)
    data_source = models.TextField()

class GeospatialFeature(models.Model):
    geometry = models.GeometryField()
