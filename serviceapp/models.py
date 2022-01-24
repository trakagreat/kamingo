import os.path
import random
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# file renaming function ----------------
def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    randomstr = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('service_photos', randomstr)


# models ----------------------------


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




    def __str__(self):
        return self.title

    def get_rating(self ):
        total = sum(int(review['rating']) for review in self.reviews.values())
        if self.reviews.count()>0:
            return total/self.reviews.count()
        else:
            return 0


class ImageModel(models.Model):
    image = models.ImageField(upload_to="service_photos", null=True)



class ReviewModel(models.Model):
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='reviews' , null=True)
    user = models.ForeignKey(User , related_name='reviews' , on_delete=models.CASCADE , null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    content = models.TextField(blank=True , null=True)
    date_added = models.DateTimeField(auto_now_add=True ,null=True ,blank=True)

    def __str__(self):
        return f"{self.rating} { self.user } {self.service}"

    class Meta:
        ordering = ['-date_added']