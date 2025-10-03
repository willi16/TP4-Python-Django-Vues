from django.db import models

class Niveau(models.Model):
    nom = models.CharField(max_length=2, unique=True)

    
    

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"
