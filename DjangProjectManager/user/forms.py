from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Manager
from django import forms

class createUserForm(forms.ModelForm):
    class Meta:
        model= Manager
        fields = ['username','mongoDbUrl','githubName','githubPassword','picture']

class createUserForm2(UserCreationForm):
    class Meta:
        model= User
        fields=['username','password1', 'password2']

