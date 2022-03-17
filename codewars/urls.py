from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('me', views.profile),
    path('add_kata', views.new_post)
]
