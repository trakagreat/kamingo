from django.forms import ModelForm
from .models import ServiceModel, ImageModel


class ServiceForm(ModelForm):
    class Meta:
        model = ServiceModel
        fields = '__all__'


class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
