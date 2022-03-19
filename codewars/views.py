from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm
from .models import User


def index(request):
    return render(request, 'index.html', {'users': ['Van', 'Maks', 'Nikita']})


def profile(request):
    return render(request, 'profile.html')


def new_post(request):
    return render(request, 'newpost.html')


def registration(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            User.objects.create(name=name, password=password, icon="")
            return HttpResponseRedirect('')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
