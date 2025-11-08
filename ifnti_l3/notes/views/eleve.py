import os
from django.http import HttpResponse
from django.conf import settings
from Templating_ifnti.controleur import generate_pdf,generate_niv_pdf  # ton contrôleur
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from notes.forms.EleveForm import EleveForm
from notes.models import eleve, niveau


@login_required
@permission_required("notes.view_eleve", raise_exception=True)
def lesEleves(request):
    listeEleves = eleve.Eleve.objects.all()
    context = {"lesEleves": listeEleves}
    return render(request, "notes/eleves.html", context)


def unEleve(request, eleve_id):
    uneleve = get_object_or_404(eleve.Eleve, id=eleve_id)
    print(uneleve)
    matiereSuivie = uneleve.matieres_suivies.all()
    context = {"uneleve": uneleve, "matiereSuivie": matiereSuivie}
    return render(request, "notes/eleve_detail.html", context)


@login_required
@permission_required("notes.add_eleve", raise_exception=True)
def add_eleve(request):
    if request.method == "POST":
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:eleves")
    else:
        form = EleveForm()
    return render(request, "notes/add_eleve.html", {"form": form})


@login_required
@permission_required("notes.change_eleve", raise_exception=True)
def update_eleve(request, eleve_id):
    eleve_update = get_object_or_404(eleve.Eleve, id=eleve_id)
    if request.method == "POST":
        form = EleveForm(request.POST, instance=eleve_update)
        if form.is_valid():
            form.save()
            return redirect("notes:eleve", eleve_id=eleve_update.id)
    else:
        form = EleveForm(instance=eleve_update)
    return render(
        request, "notes/update_eleve.html", {"form": form, "eleve": eleve_update}
    )


def listEleves(request):

    eleves = eleve.Eleve.objects.select_related("niveau").all()

    eleves_data = []
    for e in eleves:
        eleves_data.append(
            {
                "matricule": e.matricule,
                "nom": e.nom,
                "prenom": e.prenom,
                "sexe": e.sexe,
                "dateNais": (
                    e.date_naissance.strftime("%d/%m/%Y") if e.date_naissance else ""
                ),
            }
        )

    context = {
        "titre": "Liste complète des élèves",
        "eleves": eleves_data,
    }

    try:
        generate_pdf(context)
    except Exception as e:
        return HttpResponse(
            f"Erreur génération PDF : {e}", content_type="text/plain", status=500
        )

    pdf_path = os.path.join(settings.BASE_DIR, "out", "liste_eleves.pdf")
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response["Content-Disposition"] = 'inline; filename="liste_eleves.pdf"'
            return response
    else:
        return HttpResponse("PDF non trouvé après génération.", status=500)


# def listEleves(request):

#     context = {
#         "titre": "Document PDF de test",
#         "eleves": []
#     }

#     generate_pdf(context)

#     pdf_path = os.path.join(settings.BASE_DIR, "out", "liste_eleves.pdf")
#     if os.path.exists(pdf_path):
#         with open(pdf_path, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'inline; filename="liste_eleves.pdf"'
#             return response
#     else:
#         return HttpResponse("Erreur : PDF non généré", status=500)




def liste_niveauElv(request, niveau_id):
    # Récupérer le niveau via son ID
    unniveau = get_object_or_404(niveau.Niveau, id=niveau_id)

    # Récupérer les élèves de ce niveau
    eleves = eleve.Eleve.objects.filter(niveau=unniveau).select_related("niveau")

    
    eleves_data = []
    for e in eleves:
        eleves_data.append(
            {
                "matricule": e.matricule,
                "nom": e.nom,
                "prenom": e.prenom,
                "sexe": e.sexe,
                "dateNais": (
                    e.date_naissance.strftime("%d/%m/%Y") if e.date_naissance else ""
                ),
                "niveau": e.niveau.nom,
            }
        )

   
    context = {
        "titre": f"Liste des élèves du niveau ID : {niveau_id}",
        "eleves": eleves_data,
    }

    try:
        generate_niv_pdf(context)
    except Exception as e:
        return HttpResponse(
            f"Erreur génération PDF : {e}", content_type="text/plain", status=500
        )

    
    pdf_path = os.path.join(settings.BASE_DIR, "out", "liste_niveauElv.pdf")
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response["Content-Disposition"] = (
                f'inline; filename="eleves_niveau_{niveau_id}.pdf"'
            )
            return response
    else:
        return HttpResponse("PDF non trouvé après génération.", status=500)
