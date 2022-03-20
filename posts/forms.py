from django import forms
from django.contrib.auth.hashers import make_password

from .models import User, Post


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email')

    # email = forms.EmailField(label='Email')
    # username = forms.CharField(label='Имя пользователя', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), max_length=50)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), max_length=50)


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'complexity', 'language', 'link')
    solution = forms.CharField(widget=forms.Textarea, label="что-то")
