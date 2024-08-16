
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser



# Create User form
class Createuserform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(required=True)
    class Meta:
        model =CustomUser
        fields = ['first_name','last_name','email','password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']  # Set email
        user.username = self.cleaned_data['email']  # Set username to email
        if commit:
            user.save()
        return user


#Authenticate form

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))