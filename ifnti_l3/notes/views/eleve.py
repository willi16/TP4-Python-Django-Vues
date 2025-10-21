from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from notes.forms.EleveForm import EleveForm

from notes.models import eleve

def lesEleves(request):
    listeEleves = eleve.Eleve.objects.all()
    context = {'lesEleves': listeEleves}
    return render(request ,'notes/eleves.html',context)

def unEleve(request, eleve_id):
    uneleve = get_object_or_404(eleve.Eleve, id=eleve_id)
    print(uneleve)
    matiereSuivie = uneleve.matieres_suivies.all()
    context = {'uneleve': uneleve,
               'matiereSuivie' : matiereSuivie
               }
    return render(request,'notes/eleve_detail.html',context)




def add_eleve(request):
    if request.method == "POST":
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:eleves')  
    else:
        form = EleveForm()
    return render(request, 'notes/add_eleve.html', {'form': form})


def update_eleve(request, eleve_id):
    eleve_update = get_object_or_404(eleve.Eleve, id=eleve_id)
    if request.method == "POST":
        form = EleveForm(request.POST, instance=eleve_update)
        if form.is_valid():
            form.save()
            return redirect('notes:eleve', eleve_id=eleve_update.id)
    else:
        form = EleveForm(instance=eleve_update)
    return render(request, 'notes/update_eleve.html', {'form': form,'eleve': eleve_update})