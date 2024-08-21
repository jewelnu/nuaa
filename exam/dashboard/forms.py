from django import forms
from .models import Student,District, Upozilla, AddressJob
from django.core.exceptions import ValidationError
from PIL import Image as PTL_Image


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
    
    def clean_picture(self):
        pp_picture = self.cleaned_data.get("picture")
        if pp_picture:
            # Open the image to check its size
            img = PTL_Image.open(pp_picture)
            width, height = img.size
            # Check if the image size is exactly 300x300 pixels
            if width < 300 or height < 300:
                raise ValidationError('Passport image size should be minimum 300x300 pixels. Current size: {}x{}.'.format(width, height))
        return pp_picture



class AddressJobForm(forms.ModelForm):
    # Address fields
    present_address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Present Address'}))
     # Dropdown fields for present address
    present_dist = forms.ModelChoiceField(queryset=District.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    present_upozilla = forms.ModelChoiceField(queryset=Upozilla.objects.none(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    permanent_address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Permanent Address'}))
    # Dropdown fields for permanent address
    permanent_dist = forms.ModelChoiceField(queryset=District.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    permanent_upozilla = forms.ModelChoiceField(queryset=Upozilla.objects.none(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    work_address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Work Address'}))
    # Dropdown fields for work address
    work_dist = forms.ModelChoiceField(queryset=District.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    work_upozilla = forms.ModelChoiceField(queryset=Upozilla.objects.none(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = AddressJob
        fields = ['present_address', 'present_dist', 'present_upozilla', 
                  'permanent_address', 'permanent_dist', 'permanent_upozilla', 
                  'work_address', 'work_dist', 'work_upozilla']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'present_dist' in self.data:
            try:
                district_id = int(self.data.get('present_dist'))
                self.fields['present_upozilla'].queryset = Upozilla.objects.filter(dist_id=district_id).order_by('upozilla')
            except (ValueError, TypeError):
                pass
        if 'permanent_dist' in self.data:
            try:
                district_id = int(self.data.get('permanent_dist'))
                self.fields['permanent_upozilla'].queryset = Upozilla.objects.filter(dist_id=district_id).order_by('upozilla')
            except (ValueError, TypeError):
                pass
        if 'work_dist' in self.data:
            try:
                district_id = int(self.data.get('work_dist'))
                self.fields['work_upozilla'].queryset = Upozilla.objects.filter(dist_id=district_id).order_by('upozilla')
            except (ValueError, TypeError):
                pass
