from django.forms import ModelForm
from .models import ServiceModel


class ServiceForm(ModelForm):
    class Meta:
        model = ServiceModel
        fields = '__all__'
