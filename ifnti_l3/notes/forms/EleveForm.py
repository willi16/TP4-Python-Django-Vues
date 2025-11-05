from django import forms
from django.core.exceptions import ValidationError
from notes.models import Eleve, Matiere

class EleveForm(forms.ModelForm):
    
    
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'date_naissance','sexe', 'niveau','matieres_suivies','user']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'date_naissance': 'Date de naissance',
            'sexe': 'Sexe',
            'niveau': 'Niveau', 
            'matieres_suivies' : 'Matieres_suivies',
            'user' : 'Users'
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

    
    def clean(self):
        cleaned_data = super().clean()  
        niveau = cleaned_data.get('niveau')
        matieres_suivies = cleaned_data.get('matieres_suivies')

        if niveau and matieres_suivies:
            matieres_invalides = []
            for matiere in matieres_suivies:
                
                if niveau not in matiere.niveaux.all():
                    matieres_invalides.append(matiere.nom)


            if matieres_invalides:
                message = "Les matières suivantes ne sont pas disponibles pour le niveau " + str(niveau) + " : "
                for nom in matieres_invalides:
                    message += nom
                    message += " " 
                
                raise ValidationError(message)

        return cleaned_data
    

    # def save(self, commit=True):
    #     eleve = super().save(commit=False)
    #     nom = eleve.nom[:2].upper()        
    #     prenom = eleve.prenom[:2].upper()  
    #     sexe = eleve.sexe.upper()          
    #     annee = str(eleve.date_naissance.year)  
    #     eleve.matricule = f"{nom}{prenom}{sexe}{annee}"
        
    #     if commit:
    #         eleve.save()
    #         matieres_du_niveau = eleve.niveau.matieres.all()
            
    #         eleve.matieres_suivies.set(matieres_du_niveau)
            
    #     return eleve
       