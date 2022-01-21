from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServiceModel(models.Model):
    image = models.ImageField(upload_to="service_photos", null=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, related_name='category', null=True)
    cost = models.IntegerField()
    service_provider_name = models.CharField(max_length=100)
    contact = PhoneNumberField()
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    image = models.ImageField(upload_to="service_photos", null=True)

