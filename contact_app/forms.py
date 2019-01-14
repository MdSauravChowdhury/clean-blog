from django import forms
from .models import getData

class contactForm(forms.ModelForm):    
    class Meta:
        model = getData
        fields = [
            'name',
            'email',
            'phone',
            'description'
        ]

