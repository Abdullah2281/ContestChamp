from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "name", "age", "email", "password1", "password2")
        labels = {
            "username": "Handle",
        }
