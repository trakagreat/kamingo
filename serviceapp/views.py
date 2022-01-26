import requests
from django.shortcuts import render, reverse
from .forms import ServiceForm, ReviewForm
from .models import ServiceModel, ReviewModel
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .filters import ServiceFilter


# Create your views here.
# Create your views here.


class FrontPageView(View):
    def get(self, request):
        f = ServiceFilter(request.GET, queryset=ServiceModel.objects.all())
        context = {
            'filter': f,
        }
        return render(request, 'serviceapp/front_page.html', context)


# class ServiceListView(ListView):
#     model = ServiceModel
#     template_name = 'serviceapp/front_page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = ServiceFilter(self.request.GET, queryset=self.get_queryset())
#         return context
#


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
    def get(self, request, pk):
        service = ServiceModel.objects.get(pk=pk)
        review_form = ReviewForm()
        if request.user.is_authenticated:
            user_review = ReviewModel.objects.filter(service=service, user=request.user)
        else:
            user_review = None
        context = {
            'service': service,
            'form': review_form,
            'user_review': user_review,
        }

        return render(request, 'serviceapp/service_detail_page.html', context)

    def post(self, request, pk):
        review = ReviewForm(request.POST)
        service = ServiceModel.objects.get(pk=pk)
        if review.is_valid():
            new_review = review.save(commit=False)
            new_review.service = service
            new_review.user = request.user
            new_review.save()
            return HttpResponseRedirect(reverse('service-detail-page', kwargs={
                'pk': pk,
            }))

        context = {
            'service': service,
            'form': review,
        }

        return render(request, 'serviceapp/service_detail_page.html', context)
