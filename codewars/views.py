from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'users': ['Van', 'Maks', 'Nikita']})


def profile(request):
    return render(request, 'profile.html')


def new_post(request):
    return render(request, 'newpost.html')


def registration(request):
    return render(request, 'registration.html')
