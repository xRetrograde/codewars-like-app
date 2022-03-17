from django.db import models


class User(models.Model):
    # post = foreign key
    pass


class Post(models.Model):
    name = models.TextField()
    link = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
