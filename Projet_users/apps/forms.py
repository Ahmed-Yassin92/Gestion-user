from .models import User
from django import forms

class FormConnexion(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe")
    class Meta:
        model= User
        fields=['email','password']
