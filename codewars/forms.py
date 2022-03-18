from django import forms


class NameForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=30)
    password = forms.CharField(label='Пароль', max_length=25)
