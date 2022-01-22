from django.contrib import admin

from .models import ServiceModel, CategoryModel , ReviewModel

# Register your models here.

admin.site.register(ServiceModel)
admin.site.register(CategoryModel)
admin.site.register(ReviewModel)
