from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required,permission_required

from notes.models import matiere

@login_required
@permission_required('notes.view_matiere', raise_exception=True)
def lesMatieres(request):
    listeMatieres = matiere.Matiere.objects.all()
    context={'lesMatieres':listeMatieres}
    return render(request,'notes/matieres.html',context)


def uneMatiere(request, matiere_id):
    unematiere = get_object_or_404(matiere.Matiere,id=matiere_id)
    context = {'uneMatiere': unematiere}
    return render(request,'notes/matiere_detail.html',context)