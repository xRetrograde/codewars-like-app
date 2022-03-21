from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, AddPost
from .models import User, Post


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def profile(request):
    return render(request, 'profile.html', {'username': request.session.get('name'),
                                            'posts': ['lambda x: x * 2', 'print("hello world")']})


def new_post(request):
    return render(request, 'newpost.html', {'form': AddPost})


def registration(request):
    if request.session.get('email'):
        return redirect('/profile')

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(request.POST["password"])
            new_user.save()

            request.session['name'] = form.cleaned_data.get('name')
            request.session['email'] = form.cleaned_data.get('email')
            request.session['password'] = form.cleaned_data.get('password')

            return redirect('/profile')

    form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.session.get('email'):
        return redirect('/profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = get_object_or_404(User, email=form.cleaned_data.get('email'))
            if check_password(request.POST["password"], user.password):
                request.session['name'] = user.name
                request.session['email'] = user.email
                request.session['password'] = form.cleaned_data.get('password')
                return redirect('/profile')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    for key in ['name', 'email', 'password']:
        del request.session[key]

    return redirect('/')


def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
    form = AddPost()
    return render(request, 'newpost.html', {'form': form})
