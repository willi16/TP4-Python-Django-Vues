from django.contrib import admin
from .models import Eleve,Niveau,Matiere,Enseignant,Note
from .forms.EleveForm import EleveForm


class EleveAdmin(admin.ModelAdmin):
    form = EleveForm  

admin.site.register(Eleve, EleveAdmin)
# Register your models here.
# admin.site.register(Eleve)
admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Enseignant)
admin.site.register(Note)

