from django import forms
from .models import Student

class Regi_form(forms.Form):
    reg_no =forms.CharField(max_length=20,label ="Registration Number")
    gender = forms.CharField(max_length=10, label ="Gender",required=False)
