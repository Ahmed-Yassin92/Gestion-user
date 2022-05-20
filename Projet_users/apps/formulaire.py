from django import forms


class form_log(forms.Form):
    votre_nom = forms.CharField(label='votre nom', max_length=100)