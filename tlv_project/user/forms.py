from dataclasses import fields
from email.mime import image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
    
