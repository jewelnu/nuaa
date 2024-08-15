
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser


# Create User form
class Createuserform(UserCreationForm):
    class Meta:
        model =CustomUser
        fields = ['email', 'password1', 'password2']



#Authenticate form

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))