from django.urls import path
from .views import (
    index, 
    eleve, 
    matiere, 
    niveau, 
    note,
    enseignant
    #statistiquesViews
)


app_name = 'notes'

urlpatterns = [
    path('', index.index, name='index'),                  

    path('eleves/', eleve.lesEleves, name='eleves'),          
    path('eleve/<int:eleve_id>/', eleve.unEleve, name='eleve'), 

    path('matieres/', matiere.lesMatieres, name='matieres'),       
    path('matiere/<int:matiere_id>/', matiere.uneMatiere, name='matiere'),  

    path('niveau/<int:niveau_id>', niveau.unNiveau, name='niveau'), 

    path('eleve/<int:eleve_id>/matiere/<int:matiere_id>/add_note/', note.add_note, name='add_note'),

    path('matiere/<int:matiere_id>/add_notes', note.add_notes, name='add_notes'),

    path('eleve/add_eleve', eleve.add_eleve, name='add_eleve'),

    path('enseignants/', enseignant.enseignants, name='enseignants'), 
    path('enseignant/<int:enseignant_id>/', enseignant.unEnseignant, name='enseignant'), 


    path('enseignant/add_enseignant/', enseignant.add_enseignant, name='add_enseignant'),

    path('eleve/<int:eleve_id>/update_eleve/', eleve.update_eleve, name='update_eleve'),

    path('enseignant/<int:enseignant_id>/update_enseignant', enseignant.update_enseignant, name='update_enseignant'),




    # path('statistiques/',statistiquesViews.statistiques, name='stats')       
]


