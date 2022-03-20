from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    name = models.CharField("имя", max_length=50, null=False)
    email = models.EmailField("электронная почта", null=False, unique=True)
    password = models.CharField(max_length=50, null=False)

    def set_password(self, password):
        self.password = make_password(password)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField('Название', max_length=30)
    complexity = models.CharField('Сложность', max_length=3, null=False)
    language = models.CharField('Язык', max_length=30, null=False)
    link = models.CharField('Ссылка', max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.TextField(default='Ваше решение')

    def __str__(self):
        return self.author
