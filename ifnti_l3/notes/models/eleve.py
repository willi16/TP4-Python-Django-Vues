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
    
    matieres_suivies = models.ManyToManyField(
        'Matiere',
        related_name='eleves',
        blank=True
    )

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
        
        
        
    def save(self,*args,**kwargs):
        nom = self.nom[:2].upper()        
        prenom = self.prenom[:2].upper()  
        sexe = self.sexe.upper()          
        annee = str(self.date_naissance.year)  
        self.matricule = f"{nom}{prenom}{sexe}{annee}"
        
        super().save(*args,**kwargs)
        
        if not self.matieres_suivies.exists():
            matieres_du_niveau = self.niveau.matieres.all()
                
            self.matieres_suivies.set(matieres_du_niveau)
                 

    def __str__(self):
        return f"{self.id} - {self.prenom} {self.nom}"


 
          