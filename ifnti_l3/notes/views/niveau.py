from django.shortcuts import render, get_object_or_404
from notes.models import niveau

def unNiveau(request,niveau_id):
    unniveau = get_object_or_404(niveau.Niveau, id=niveau_id)
    context = {'unniveau': unniveau}
    return render(request, 'notes/niveau.html', context)
  


    