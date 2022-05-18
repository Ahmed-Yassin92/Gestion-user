from django.db import models
from django.utils import timezone


class Users (models.Model):
    noms = models.CharField(max_length=100)
    prenom = models.CharField(max_length=60)
    Date = models.DateField(default=timezone.now)
