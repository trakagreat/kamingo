from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class ServiceModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    cost = models.IntegerField()
    service_provider_name = models.CharField(max_length=100)
    contact = PhoneNumberField()
