from django.db import models

# Create your models here.

class PricingConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    distanceBasePrice = models.CharField(max_length=200)
    distanceAdditionalPrice = models.CharField(max_length=200)
    timeMultiplierFactor = models.CharField(max_length=200)
    distance = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.distanceBasePrice
