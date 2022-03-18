from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('me', views.profile),
    path('new_post', views.new_post),
    path('registration', views.registration)
]
