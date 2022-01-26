import django_filters
from .models import ServiceModel


class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = ServiceModel
        fields = ['category']
