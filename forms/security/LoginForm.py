from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'login-form__input'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    password.widget.attrs.update({'class': 'login-form__input login-form__password'})






