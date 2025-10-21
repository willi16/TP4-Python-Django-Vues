from django.shortcuts import render, redirect, get_object_or_404
from notes.forms.EnseignantForm import EnseignantForm
from notes.models import Enseignant


def enseignants(request):
    listeEnseignants = Enseignant.objects.all()
    context = {'enseignants': listeEnseignants}
    return render(request ,'notes/enseignants.html',context)



def unEnseignant(request, enseignant_id):
    unenseignant = get_object_or_404(Enseignant, id=enseignant_id)  
    context = {'unenseignant': unenseignant}
    return render(request,'notes/enseignant_detail.html',context)


def add_enseignant(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'notes/add_enseignant.html', {'form': form})


def update_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    if request.method == "POST":
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('notes:enseignant', enseignant_id=enseignant.id)
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'notes/update_enseignant.html', {'form': form,'enseignant': enseignant})