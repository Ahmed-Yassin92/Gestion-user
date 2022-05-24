from django.db import models
from django.utils import timezone
from statistics import mode
from django import forms


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=60)
    Date = models.DateField(default=timezone.now)
    email_user = models.CharField(max_length=50,default='google@gmail.com')
    password_user = forms.CharField(max_length=50,widget=forms.PasswordInput, default='0000')


class Sessions (models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now)


class FormConnexion(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe")
    class Meta:
        model= User()
        fields=['email','password']

    