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
    name = models.CharField('Название', max_length=20)
    difficulty = models.IntegerField(default=8)
    language = models.CharField('Язык', max_length=15)
    link = models.URLField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField(default='Ваше решение')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name

    def set_fields(self, difficulty, link, solution, author, date):
        self.difficulty = difficulty
        self.link = link
        self.code = solution
        self.author = author
        self.date = date
