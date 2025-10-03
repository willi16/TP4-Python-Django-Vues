from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from notes.models import eleve

def lesEleves(request):
    listeEleves = eleve.Eleve.objects.all()
    context = {'lesEleves': listeEleves}
    return render(request ,'notes/eleves.html',context)

def unEleve(request, eleve_id):
    uneleve = get_object_or_404(eleve.Eleve, id=eleve_id)
    context = {'uneleve': uneleve}
    return render(request,'notes/eleve_detail.html',context)


 