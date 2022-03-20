from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from .models import User, Post



def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def profile(request):
    return render(request, 'profile.html', {'username': request.session.get('name'),
                                            'posts': ['lambda x: x * 2', 'print("hello world")']})


def new_post(request):
    return render(request, 'newpost.html')


def registration(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(request.POST["password"])
            new_user.save()
            return HttpResponseRedirect('')

    form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            user = User.objects.get(email=form.cleaned_data.get("email"))
            if check_password(request.POST["password"], user.password):
                return HttpResponse("Ну проходи")
            else:
                return HttpResponse("уходи о больше никогда не приходи")
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
