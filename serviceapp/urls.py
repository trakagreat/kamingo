from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front-page'),
    path('service-form', views.ServiceFormView.as_view(), name='service_form_url'),

]
