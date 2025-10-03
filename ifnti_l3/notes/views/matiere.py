from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from notes.models import matiere

def lesMatieres(request):
    listeMatieres = matiere.Matiere.objects.all()
    context={'lesMatieres':listeMatieres}
    return render(request,'notes/matieres.html',context)

def uneMatiere(request, matiere_id):
    unematiere = get_object_or_404(matiere.Matiere,id=matiere_id)
    context = {'uneMatiere': unematiere}
    return render(request,'notes/matiere_detail.html',context)