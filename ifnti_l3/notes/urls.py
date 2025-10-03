from django.urls import path
from .views import index, eleve, matiere, niveau

app_name = 'notes'

urlpatterns = [
    path('', index.index, name='index'),                  

    path('eleves/', eleve.lesEleves, name='eleves'),          
    path('eleve/<int:eleve_id>/', eleve.unEleve, name='eleve'), 

    path('matieres/', matiere.lesMatieres, name='matieres'),       
    path('matiere/<int:matiere_id>/', matiere.uneMatiere, name='matiere'),  

    path('niveau/<int:niveau_id>', niveau.unNiveau, name='niveau'),         
]