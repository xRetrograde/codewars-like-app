from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default='1234')


class Post(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
