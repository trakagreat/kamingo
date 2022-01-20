from django.shortcuts import render, reverse
from .forms import ServiceForm , ImageForm
from .models import ServiceModel
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
# Create your views here.
def front_page(request):
    services = ServiceModel.objects.all()
    return render(request, 'serviceapp/front_page.html', {
        'services': services
    })


class ServiceFormView(View):
    def get(self, request):
        service_form = ServiceForm()
        # service_form = ImageForm()
        return render(request, 'serviceapp/service_form.html', {
            "form": service_form ,
        })

    def post(self, request):
        service = ServiceForm(request.POST)
        # service = ImageForm(request.POST , request.FILES)
        if service.is_valid():
            new_service = service.save(commit=False)
            new_service.save()
            return HttpResponseRedirect(reverse('front-page'))
        else:
            return render(request, 'serviceapp/service_form.html', {
                "form": service
            })
