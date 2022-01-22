from django.shortcuts import render, reverse
from .forms import ServiceForm, ReviewForm
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
            "form": service_form,
        })

    def post(self, request):
        service = ServiceForm(request.POST, request.FILES)
        # service = ImageForm(request.POST , request.FILES)
        if service.is_valid():
            new_service = service.save(commit=False)
            new_service.save()
            return HttpResponseRedirect(reverse('front-page'))
        else:
            return render(request, 'serviceapp/service_form.html', {
                "form": service
            })

class ServiceDetailView(View):
    def get(self , request ,pk):
        service = ServiceModel.objects.get(pk=pk)
        review_form = ReviewForm()
        context={
          'service' : service,
            'form' : review_form,
        }

        return render( request , 'serviceapp/service_detail_page.html', context )
    def post(self , request ,pk):
        review = ReviewForm(request.POST)
        service = ServiceModel.objects.get(pk=pk)
        if review.is_valid():
            new_review = review.save( commit=False)
            new_review.save()
            service.review = new_review
            service.save()
        context = {
            'service': service,
            'form': review,
        }

        return render(request, 'serviceapp/service_detail_page.html', context)
