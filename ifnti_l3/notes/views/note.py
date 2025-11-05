from django.http import HttpResponse,Http404,HttpResponseForbidden
from django.contrib.auth.decorators import login_required,permission_required

from  django.shortcuts import render , get_object_or_404, redirect
from notes.models import Eleve, Matiere, Note
from notes.forms.Noteform import NoteForm

# def add_note(request, eleve_id, matiere_id):
#     eleve = get_object_or_404(Eleve, id=eleve_id)
#     matiere = get_object_or_404(Matiere, id=matiere_id)
    

#     if request.method == "POST":
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.eleve = eleve
#             note.matiere = matiere
#             note.save()
#             return redirect('notes:eleve', eleve_id=eleve.id)
#     #     valeur = request.POST.get("valeur")
#     #     Note.objects.create(
#     #         eleve=eleve,
#     #         matiere=matiere,
#     #         valeur=valeur
#     #     )
#     #     return HttpResponse("Note ajoutée avec succès !")

#     else:
#         form = NoteForm()
#         if matiere in eleve.matieres_suivies.all():
#             return render(request, 'notes/add_note.html',
#                 {'eleve': eleve,
#                 'matiere': matiere,
#                 'form': form
#                 }
#             )
#         else:
#              return HttpResponse("ohhhhhhh")


@login_required
@permission_required('notes.add_note')
def add_note(request, eleve_id, matiere_id):
    eleve = get_object_or_404(Eleve, id=eleve_id)
    matiere = get_object_or_404(Matiere, id=matiere_id)

    if matiere not in eleve.matieres_suivies.all():
        return HttpResponse("L'élève ne suit pas cette matière.")
    
    group_names = [group.name for group in request.user.groups.all()]

   
    if 'enseignant' in group_names or 'directeur' in group_names:
       
        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.eleve = eleve
                note.matiere = matiere
                note.save()
                return redirect('notes:eleve', eleve_id=eleve.id)
        else:
            form = NoteForm()  
        return render(request,'notes/add_note.html', {
            'eleve': eleve,
            'matiere': matiere,
            'form': form
        })

    return HttpResponseForbidden("Vous n'avez pas la permission d'ajouter une note.")


# @login_required
# @permission_required('notes.add_note')
def add_notes(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    # eleves = matiere.matiere_eleve_set.all()
    eleves = matiere.eleves.all() 

    if not eleves:
        return HttpResponse("Aucun élève n'est inscrit dans cette matière.")

    if request.method == "POST":
        for eleve in eleves:
            valeur = request.POST.get(f'note_{eleve.id}')
            if valeur:
                form = NoteForm() 
                if form.is_valid():
                    Note.objects.update_or_create(
                        eleve=eleve,
                        matiere=matiere,
                        defaults={'valeur': valeur}
                    )
        return redirect('notes:matiere', matiere_id=matiere.id)
    else:
       
        formset = []
        for eleve in eleves:
            note = Note.objects.filter(eleve=eleve, matiere=matiere).first()
            initial = {'valeur': note.valeur} if note else {}
            form = NoteForm(initial=initial)
            formset.append({'eleve': eleve, 'form': form})
        return render(request, 'notes/add_notes.html', {
            'matiere': matiere,
            'formset': formset
        })