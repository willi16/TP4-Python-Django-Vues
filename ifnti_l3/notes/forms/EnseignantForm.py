from django import forms
from django.core.exceptions import ValidationError

from notes.models import Enseignant

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'date_naissance','sexe']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'date_naissance': 'Date de naissance',
            'sexe': 'Sexe',    
        }
       
       
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if any(char.isdigit() for char in nom):
            raise ValidationError("Le nom ne doit pas contenir de chiffres.")
        return nom.strip()

    def clean_prenom(self):
        prenom = self.cleaned_data['prenom']
        if any(char.isdigit() for char in prenom):
            raise ValidationError("Le prénom ne doit pas contenir de chiffres.")
        return prenom.strip()
    