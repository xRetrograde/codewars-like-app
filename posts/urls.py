from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.profile),
    path('registration', views.registration),
    path('login', views.login),
    path('add-post', views.add_post),
    path('logout', views.logout),
    path('post/<int:post_id>', views.post)
]
