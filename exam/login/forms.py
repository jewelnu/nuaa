
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
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)