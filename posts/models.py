from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=50, null=False)

    def set_password(self, password):
        self.password = make_password(password)


class Post(models.Model):
    name = models.CharField(max_length=30)
    complexity = models.CharField(max_length=3, null=False)
    language = models.CharField(max_length=30, null=False)
    link = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
