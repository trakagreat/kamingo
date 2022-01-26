from django.urls import path
from . import views
from django_filters.views import object_filter
from serviceapp.models import ServiceModel

urlpatterns = [
    path('', views.FrontPageView.as_view(), name='front-page'),
    path('service-form', views.ServiceFormView.as_view(), name='service_form_url'),
    path('service-detail/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail-page'),

]
