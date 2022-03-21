from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    name = models.CharField("Имя", max_length=20, null=False)
    email = models.EmailField("Электронная почта", null=False, unique=True)
    password = models.CharField(max_length=20, null=False)

    def set_password(self, password):
        self.password = make_password(password)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField('Имя', max_length=20)
    difficulty = models.IntegerField('Сложность', default=8, null=False)
    language = models.CharField('Язык', max_length=15, null=False)
    link = models.URLField('Ссылка', max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.TextField(default='Ваше решение')

    def __str__(self):
        return self.author
