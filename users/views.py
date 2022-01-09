from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Create your views here.


def login_page(request):
    return render(request, 'users/login.html')


def register_page(request):
    form = RegisterUserForm
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'users/register.html', {
        'form': form
    })
