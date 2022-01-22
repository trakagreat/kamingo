import os.path
import random
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator


# file renaming function ----------------
def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    randomstr = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('service_photos', randomstr)


# models ----------------------------
class ReviewModel(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServiceModel(models.Model):
    image = models.ImageField(upload_to=path_and_rename, null=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, related_name='category', null=True)
    cost = models.IntegerField()
    service_provider_name = models.CharField(max_length=100)
    contact = PhoneNumberField()
    address = models.CharField(max_length=200, null=True)
    review = models.OneToOneField(ReviewModel, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    image = models.ImageField(upload_to="service_photos", null=True)
