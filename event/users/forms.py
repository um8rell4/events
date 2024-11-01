from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "id": "username", "name": "username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "id": "username", "name": "username"}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"type": "password", "id": "password", "name": "password"}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"type": "password", "id": "password", "name": "password"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

