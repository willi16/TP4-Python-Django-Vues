from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from notes.models import (
    eleve,
    note,
    niveau,
    matiere,
    enseignant
)
def statistiques(request):
    nb_eleves = eleve.Eleve.objects.count()
    nb_enseignants = enseignant.Enseignant.objects.count()
    nb_matieres = matiere.Matiere.objects.count()
    nb_notes = note.Note.objects.count()


    moyenne_generale_par_eleve = []
    eleves = eleve.Eleve.objects.annotate(moyenne_generale=Avg(""))

    for e in eleves:
        moyennes_eleve = note.Note.objects.aggregate(moyenne_generale=Avg("notes__valeur"))



    context = {
        "nb_eleves" : nb_eleves,
        "nb_enseignants" : nb_enseignants,
        "nb_matieres" : nb_matieres,
        "nb_notes" : nb_notes
    }



    return render(request,'',context)
    return HttpResponse("hallo")