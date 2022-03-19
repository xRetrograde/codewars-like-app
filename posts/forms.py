from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=30)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
