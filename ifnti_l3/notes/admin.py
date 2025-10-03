from django.contrib import admin
from .models import Eleve,Niveau,Matiere,Enseignant


# Register your models here.
admin.site.register(Eleve)
admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Enseignant)
