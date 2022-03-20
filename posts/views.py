from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User, Post


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def profile(request):
    print(request.session.get('name'))
    return render(request, 'profile.html', {'username': 'name',
                                            'posts': ['lambda x: x * 2', 'print("hello world")']})


def new_post(request):
    return render(request, 'newpost.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            User.objects.create(name=name, password=password)
            return redirect('/')

    form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
