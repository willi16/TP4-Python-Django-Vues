from django.db import models
from .eleve import Eleve
from .matiere import Matiere

class Note(models.Model):
    eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE, related_name='notes')
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE, related_name='notes')
    valeur = models.DecimalField('Note', max_digits=5, decimal_places=2,null=True,blank=True)
    date = models.DateField("Date", auto_now_add=True)
      

    def __str__(self):
        return f"{self.eleve} - {self.matiere} : {self.valeur}"

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        unique_together = ('eleve', 'matiere','date')
        
 
        
        
        
        
        

