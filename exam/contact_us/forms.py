from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )


class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

