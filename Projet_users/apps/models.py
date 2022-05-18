from django.db import models
from django.utils import timezone


class users (models.Model):
    noms = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=60)
    Date = models.DateField(timezone.now())
