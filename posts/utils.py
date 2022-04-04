from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from .models import User


def auth_required(view):
    def wrapped(request):
        user = User.objects.filter(email=request.session.get('email')).exists()
        if user:
            return view(request)

        return redirect('/login')

    return wrapped


def unauth_required(view):
    def wrapped(request):
        if 'name' and 'email' in request.session:
            return redirect('/profile')

        return view(request)

    return wrapped


def set_session_info(request, name, email, password):
    request.session['name'] = name
    request.session['email'] = email
    request.session['password'] = make_password(password)
