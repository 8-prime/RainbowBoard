from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    entry_guid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    summary = models.TextField()
    published = models.DateTimeField()
    link = models.URLField()
    images = ArrayField(models.URLField(), null=True)
    cold_rent = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    warm_rent = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    area = models.FloatField()
    text = models.TextField()
