from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


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


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class EditUserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False,
                          widget=forms.Textarea(attrs={"class": "form-control",
                                                        "rows": 3}))
    profile_picture = forms.ImageField(widget=forms.FileInput({"class": "form-control"}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise ValidationError("Email already exists!")
        return email
