from django import forms
from django.contrib.auth.hashers import make_password

from .models import User, Post


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email')

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), max_length=20)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), max_length=20)


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'language')

    difficulty = forms.IntegerField(max_value=8, label='Сложность')
    link = forms.URLField(max_length=200, label='Ссылка')
    solution = forms.CharField(widget=forms.Textarea, label="Что-то")
