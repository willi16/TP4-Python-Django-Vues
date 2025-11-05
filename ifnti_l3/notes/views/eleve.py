from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from notes.forms.EleveForm import EleveForm
from notes.models import eleve


@login_required
@permission_required('notes.view_eleve', raise_exception=True)
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



@login_required
@permission_required('notes.add_eleve', raise_exception=True)
def add_eleve(request):
    if request.method == "POST":
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:eleves')  
    else:
        form = EleveForm()
    return render(request, 'notes/add_eleve.html', {'form': form})

@login_required
@permission_required('notes.change_eleve', raise_exception=True)
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