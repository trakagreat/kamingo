from django.forms import ModelForm
from .models import ServiceModel, ImageModel, ReviewModel
from django import forms

class ServiceForm(ModelForm):
    class Meta:
        model = ServiceModel
        fields = '__all__'
        exclude = ('review',)
        widgets ={
            'title': forms.TextInput(attrs={ 'class': 'form-control' }),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'service_provider_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),



        }



class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['rating', 'content']
        labels = {
            'rating': 'rating',
            'content': 'review'
        }
