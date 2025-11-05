from django.contrib.auth.models import User
from django.db import models

class Personne(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenom = models.CharField("Prénom", max_length=100)
    sexe = models.CharField("Sexe",max_length=1,choices=[('F','Féminin'),('M','Masculin')])
    date_naissance = models.DateField("Date de naissance")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True 

    def __str__(self):
        return f"{self.prenom} {self.nom}"
