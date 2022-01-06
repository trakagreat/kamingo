from django.shortcuts import render
from .forms import ServiceForm


# Create your views here.

def service_form(request):
    form = ServiceForm()
    return render(request, 'serviceapp/service_form.html', {
        "form": form
    })
