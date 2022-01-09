from django.shortcuts import render
from .forms import ServiceForm
from .models import ServiceModel


# Create your views here.
# Create your views here.
def front_page(request):
    return render(request, 'base.html')


def service_form_view(request):
    service_form = ServiceForm()
    if request.method == "POST":
        service = ServiceForm(request.POST)
        if service.is_valid():
            new_service = service.save(commit=True)
    return render(request, 'serviceapp/service_form.html', {
        "form": service_form
    })
