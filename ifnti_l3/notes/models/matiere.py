from django.db import models
from .enseignant import Enseignant
from .eleve import Eleve
from .niveau import Niveau


class Matiere(models.Model):
    nom = models.CharField("Nom de la matière", max_length=50, unique=True)
    enseignant = models.ForeignKey(
        'Enseignant',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='matieres'
    )
    niveaux = models.ManyToManyField(
        'Niveau',
        null=True,
        blank=True,
        related_name='matieres'
    )
    

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"

    def __str__(self):
        return f"{self.nom} "

    def nb_eleves(self):
        return self.eleves.count()
    nb_eleves.short_description = "Nombre d'élèves"
