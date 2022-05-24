from .models import User
from django import forms

class FormInscription(forms.ModelForm): 
    nom = forms.CharField(max_length=50,label="Nom" )
    prenom = forms.CharField(max_length=50, label="Prenom")
    email = forms.EmailField(max_length=50, label="Email")
    password = forms.CharField(widget = forms.PasswordInput,max_length=16, label="Mot de passe")

class FormConnexion(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe")
    class Meta:
        model= User
        fields=['email','password']
