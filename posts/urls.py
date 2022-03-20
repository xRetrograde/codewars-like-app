from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.profile),
    path('new-post', views.new_post),
    path('registration', views.registration),
    path('login', views.login),
    path('add-post', views.NewPost)
]
