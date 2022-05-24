from msilib.schema import Class
from django.db import models
from django.utils import timezone



class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=60)
    Date = models.DateField(default=timezone.now)
    email_user = models.CharField(max_length=50,default='google@gmail.com')
    password_user = models.CharField(max_length=50, default='0000')


class Sessions (models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now)
