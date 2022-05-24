from .models import User
from django import forms



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class FormConnexion(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe")
    class Meta:
        model= User()
        fields=['email','password']

