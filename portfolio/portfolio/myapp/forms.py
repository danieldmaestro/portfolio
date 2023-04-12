from django import forms
from.models import Visitor

class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ('name', 'email', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'id': "name", 'placeholder': "Your Name"}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'id': "email", 'placeholder': "Your Email"}),
            'message': forms.Textarea(attrs={'class': "form-control", 'rows': '5', 'id': "message", 'placeholder': "Your Message"})
        }
    