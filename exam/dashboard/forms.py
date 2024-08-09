from django import forms

class Regi_form(forms.Form):
    reg_no =forms.CharField(max_length=20,label ="Registration Number")