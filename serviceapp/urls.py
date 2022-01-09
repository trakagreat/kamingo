from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page),
    path('service-form', views.service_form_view, name='service_form_url')
]
