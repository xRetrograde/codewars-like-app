from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .models import User


def index(request):
    return render(request, 'index.html', {'users': ['Van', 'Maks', 'Nikita']})


def profile(request):
    return render(request, 'profile.html')


def new_post(request):
    return render(request, 'newpost.html')


def registration(request):
    if request.method == 'POST':

        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            User.objects.create(name=name, icon="")
            return HttpResponseRedirect('')

    else:
        form = NameForm()

    return render(request, 'registration.html', {'form': form})
