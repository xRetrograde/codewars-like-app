from django import forms
from django.contrib.auth.hashers import make_password

from .models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password')

    # email = forms.EmailField(label='Email')
    # username = forms.CharField(label='Имя пользователя', max_length=50)
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), max_length=50)


