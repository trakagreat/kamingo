from django.shortcuts import render
from .forms import ServiceForm
from .models import ServiceModel


# Create your views here.
# Create your views here.
def front_page(request):
    return render( request, 'base.html')

def service_form(request):
    form = ServiceForm()
    return render(request, 'serviceapp/service_form.html', {
        "form": form
    })
