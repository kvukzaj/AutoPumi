from django import forms
from .models import Contact

class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'phone', 'email', 'message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'phone', 'email', 'message']
