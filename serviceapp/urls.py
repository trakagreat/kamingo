from django.urls import path
from . import views
from django_filters.views import object_filter
from serviceapp.models import ServiceModel

urlpatterns = [
    path('', views.FrontPageView.as_view(), name='front-page'),
    path('service-form', views.ServiceFormView.as_view(), name='service_form_url'),
    path('service-form/<slug:slug>/description', views.ServiceFormDesView.as_view(), name='service_form_des_url'),
    path('service-detail/<slug:slug>', views.ServiceDetailView.as_view(), name='service-detail-page'),

]
