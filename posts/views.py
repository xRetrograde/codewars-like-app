from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, AddPost
from .models import User, Post
from .utils import auth_required, unauth_required


def index(request):
    context = {'posts': Post.objects.order_by('-date')}
    return render(request, 'index.html', context)


@auth_required
def profile(request):
    context = {'username': request.session.get('name'),
               'posts': ['lambda x: x * 2', 'print("hello world")']}

    return render(request, 'profile.html', context)


@unauth_required
def registration(request):
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


@unauth_required
def login(request):
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


@auth_required
def logout(request):
    request.session.clear()
    return redirect('/')


@auth_required
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            email = request.session['email']
            user = User.objects.get(email=email)
            new_form = form.save(commit=False)
            difficulty = form.cleaned_data.get('difficulty')
            link = form.cleaned_data.get('link')
            code = form.cleaned_data.get('code')
            new_form.set_fields(difficulty, link, code, user)
            new_form.save()

    form = AddPost()
    return render(request, 'newpost.html', {'form': form})


def post(request, post_id):
    context = {'post_id': post_id,
               'post': Post.objects.get(pk=post_id)}
    return render(request, 'post.html', context)
