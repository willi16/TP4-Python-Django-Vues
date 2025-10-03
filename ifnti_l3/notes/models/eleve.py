from django.db import models
from .personne import Personne
from .niveau import Niveau

class Eleve(Personne):
    niveau = models.ForeignKey(
        'Niveau',
        on_delete=models.CASCADE,
        related_name='eleves'
    )
    matricule = models.CharField("Matricule", max_length=20, unique=True)

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"

    def __str__(self):
        return f"{self.id} - {self.prenom} {self.nom}"
