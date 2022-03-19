from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=500)
    password = models.CharField(max_length=30, null=False)


class Post(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
