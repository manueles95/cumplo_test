from django.db import models


class SeriesIndex(models.Model):
    series_id = models.CharField(max_length=10, primary_key=True)
    front_identifier = models.CharField(max_length=3)
    description = models.CharField(max_length=100)

class TiieIndex(models.Model):
    tiie_id = models.CharField(max_length=10, primary_key=True)
    term = models.IntegerField()
    description = models.CharField(max_length=100)
