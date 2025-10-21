from django.db import models
from .eleve import Eleve
from .matiere import Matiere
from django.core.validators import MinValueValidator, MaxValueValidator

class Note(models.Model):
    eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE, related_name='notes')
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE, related_name='notes')
    valeur = models.FloatField(
        validators=[
            MinValueValidator(0.0, message="La note ne peut pas être inférieure à 0."),
            MaxValueValidator(20.0, message="La note ne peut pas être supérieure à 20.")
        ]
    )
    date = models.DateField("Date", auto_now_add=True)
      

    def __str__(self):
        return f"{self.eleve} - {self.matiere} : {self.valeur}"

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        # unique_together = ('eleve', 'matiere','date')
        
 
        
        
        
        
        

