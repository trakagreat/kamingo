from django.forms import ModelForm
from .models import ServiceModel, ImageModel , ReviewModel


class ServiceForm(ModelForm):
    class Meta:
        model = ServiceModel
        fields = '__all__'
        exclude = ('rating',)


class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'



class ReviewForm(ModelForm):
    class Meta:
        model =ReviewModel
        fields = '__all__'