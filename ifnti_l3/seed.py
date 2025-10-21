import os
import django
import random 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifnti_l3.settings')
django.setup()
from notes.models.eleve import Eleve
from notes.models.niveau import Niveau
Niveau.objects.all().delete()
Eleve.objects.all().delete()

for i in range(1,4):
    Niveau.objects.create(
        nom = f"L{i}"
    )


for i in range(10):
    Eleve.objects.create(
        matricule = f"Matricule{i}",
        nom = f"Tamba{i}",
        prenom = f"Léon{i}",
        sexe="M",
        date_naissance="2000-01-01",
        niveau = random.choice(Niveau.objects.all())
    )



