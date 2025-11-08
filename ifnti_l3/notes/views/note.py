import os
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Eleve, Matiere, Note
from notes.forms.Noteform import NoteForm
from Templating_ifnti.controleur import generate_note_pdf,generate_synthese_pdf

from django.conf import settings

from django.db.models import Avg



@login_required
@permission_required("notes.add_note")
def add_note(request, eleve_id, matiere_id):
    eleve = get_object_or_404(Eleve, id=eleve_id)
    matiere = get_object_or_404(Matiere, id=matiere_id)

    if matiere not in eleve.matieres_suivies.all():
        return HttpResponse("L'élève ne suit pas cette matière.")

    group_names = [group.name for group in request.user.groups.all()]

    if "enseignant" in group_names or "directeur" in group_names:

        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.eleve = eleve
                note.matiere = matiere
                note.save()
                return redirect("notes:eleve", eleve_id=eleve.id)
        else:
            form = NoteForm()
        return render(
            request,
            "notes/add_note.html",
            {"eleve": eleve, "matiere": matiere, "form": form},
        )

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
            valeur = request.POST.get(f"note_{eleve.id}")
            if valeur:
                form = NoteForm()
                if form.is_valid():
                    Note.objects.update_or_create(
                        eleve=eleve, matiere=matiere, defaults={"valeur": valeur}
                    )
        return redirect("notes:matiere", matiere_id=matiere.id)
    else:

        formset = []
        for eleve in eleves:
            note = Note.objects.filter(eleve=eleve, matiere=matiere).first()
            initial = {"valeur": note.valeur} if note else {}
            form = NoteForm(initial=initial)
            formset.append({"eleve": eleve, "form": form})
        return render(
            request, "notes/add_notes.html", {"matiere": matiere, "formset": formset}
        )


def notesEleves(request, matiere_id):
    unematiere = get_object_or_404(Matiere, id=matiere_id)

    # Récupérer les notes de la matière
    notes = Note.objects.filter(matiere=unematiere).select_related("eleve")

    notes_data = []
    for n in notes:
        notes_data.append(
            {
                "nom": n.eleve.nom,
                "prenom": n.eleve.prenom,
                "matricule": n.eleve.matricule,
                "note": float(n.valeur),
                "dateNais": n.eleve.date_naissance.strftime("%d/%m/%Y"),
                "matiere": n.matiere.nom
            }
        )

    context = {
        "titre": f"Notes de la matière : {unematiere.nom}",
        "notes": notes_data,
        
    }

    try:
        generate_note_pdf(context)
    except Exception as e:
        return HttpResponse(
            f"Erreur génération PDF : {e}", content_type="text/plain", status=500
        )

    pdf_path = os.path.join(settings.BASE_DIR, "out", "notesEleves.pdf")
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response["Content-Disposition"] = (
                f'inline; filename="notes_{unematiere.nom}.pdf"'
            )
            return response
    else:
        return HttpResponse("PDF non trouvé après génération.", status=500)
    
    


def notesSynthese(request):
    
    moyennes = Note.objects.values(
        'eleve__matricule',
        'eleve__nom',
        'eleve__prenom',
        'matiere__nom'
    ).annotate(moyenne=Avg('valeur')).order_by('eleve__nom', 'matiere__nom')

    synthese_data = []
    for m in moyennes:
        synthese_data.append({
            "matricule": m['eleve__matricule'],
            "nom": m['eleve__nom'],
            "prenom": m['eleve__prenom'],
            "matiere": m['matiere__nom'],
            "moyenne": round(float(m['moyenne']), 2),
        })

    context = {
        "titre": "Synthèse des moyennes par élève et par matière",
        "synthese": synthese_data,
    }

    try:
        generate_synthese_pdf(context)
    except Exception as e:
        return HttpResponse(f"Erreur génération PDF : {e}", content_type="text/plain", status=500)

    pdf_path = os.path.join(settings.BASE_DIR, "out", "notesSyntheses.pdf")
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="synthese_notes.pdf"'
            return response
    else:
        return HttpResponse("PDF non trouvé après génération.", status=500)
