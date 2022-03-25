from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта', max_length=30, unique=True)
    password = models.CharField(max_length=20)

    def set_password(self, password):
        self.password = make_password(password)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=20)
    difficulty = models.IntegerField(default=8)
    language = models.CharField(max_length=15)
    link = models.URLField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.TextField(default='Ваше решение')

    def __str__(self):
        return self.author
