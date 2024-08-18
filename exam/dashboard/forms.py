from django import forms
from .models import Student

class Regi_form(forms.Form):
    reg_no =forms.CharField(max_length=20,label ="Registration Number")
    gender = forms.CharField(max_length=10, label ="Gender",required=False)
    marital_status = forms.CharField(max_length=20,required=False)
    nationality = forms.CharField(max_length=20,required=False)
    date_of_birth = forms.DateField(label="Date of Birth",required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    spouse_name= forms.CharField(max_length=50,label= "Spouse Name", required=False, widget= forms.TextInput(attrs={'class': 'form-control'}))
    number_of_children = forms.IntegerField(label="Number of Children", required=False,widget= forms.NumberInput(attrs={'class': 'form-control'}))
    picture = forms.ImageField(label="Upload Picture",required=False,widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Student
        fields = [
            'reg_no','gender','date_of_birth', 'marital_status', 
            'nationality', 'spouse_name', 'number_of_children', 
            'picture'
        ]
    