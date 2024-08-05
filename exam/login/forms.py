
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


# Create User form
class Createuserform(UserCreationForm):
    class Meta:
        model =User
        fields = ['username', 'email', 'password1', 'password2']



#Authenticate form

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='UserName',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))