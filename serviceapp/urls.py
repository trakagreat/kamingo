from django.urls import path
from . import views

urlpatterns = [
    path('service-form', views.service_form)
]
