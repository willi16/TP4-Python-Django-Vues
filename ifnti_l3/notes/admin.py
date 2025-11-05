from django.contrib import admin
from .models import Eleve,Niveau,Matiere,Enseignant,Note
from .forms.EleveForm import EleveForm

class EleveAdmin(admin.ModelAdmin):
    form = EleveForm  
    list_display = ('nom', 'prenom', 'niveau', 'date_naissance')
    list_display_links = ('nom', 'prenom')
    list_filter = ('niveau', 'date_naissance')
    search_fields = ('nom', 'prenom')
    list_per_page = 20
    date_hierarchy = 'date_naissance'
    sortable_by = ('nom', 'prenom', 'date_naissance')
    
    readonly_fields = ('matricule',)  
    save_as = True
    save_on_top = True
    
    filter_horizontal = ('matieres_suivies',)
    
    
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }
        js = ('js/admin_custom.js')

admin.site.register(Eleve, EleveAdmin)

admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Enseignant)
admin.site.register(Note)

    