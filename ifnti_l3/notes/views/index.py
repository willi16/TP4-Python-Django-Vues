# from django.shortcuts import render

# def index(request):
#     return render(request, "notes/index.html")
from django.http import HttpResponseForbidden
from django.shortcuts import render
from notes.models import Eleve, Matiere, Enseignant

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Accès refusé : vous devez être connecté.")
    
    nb_eleves = Eleve.objects.count()
    nb_matieres = Matiere.objects.count()
    nb_enseignants = Enseignant.objects.count()

    context = {
        'nb_eleves': nb_eleves,
        'nb_matieres': nb_matieres,
        'nb_enseignants': nb_enseignants,
    }
    return render(request, 'notes/index.html', context)