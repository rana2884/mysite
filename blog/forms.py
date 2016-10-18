from django import forms
from captcha.fields import CaptchaField
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']