from django import forms
from .models import Ngo

class NGO_form(forms.ModelForm):
    class Meta:
        model= Ngo
        fields=['name' , 'objective' , 'description' , 'scope' , 'reg_no' , 'website' , 'email' , 'contribution' , 'image']