import os
import subprocess
from os.path import dirname, abspath
from jinja2 import Environment
from latex import build_pdf

def generate_pdf(context) :

    j2_env = Environment(
        variable_start_string="\VAR{",variable_end_string="}",
        block_start_string="\BLOCK{",block_end_string="}", 
        comment_start_string="\COMMENT{",comment_end_string="}"
        )
   
    #fichier à lire contenant le template avec les balises
    fichier_in = open("ifnti/liste_eleves.tex", 'r')
    #fichier en sortie accueillant les données fournies
    fichier_out = open("out/template_out.tex", 'w')
    template = fichier_in.read() #lecture du template
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__)) + "/out/images/"
    
    j2_template = j2_env.from_string(template)
    # écriture dans le fichier en sortie
    fichier_out.write(j2_template.render(monContext))
    fichier_out.close()
    
    mon_pdf = build_pdf(open("out/template_out.tex", 'r'))
    mon_pdf.save_to("out/liste_eleves.pdf")
    
    fichier_in.close()
    
def generate_niv_pdf(context) :

    j2_env = Environment(
        variable_start_string="\VAR{",variable_end_string="}",
        block_start_string="\BLOCK{",block_end_string="}", 
        comment_start_string="\COMMENT{",comment_end_string="}"
        )
   
    #fichier à lire contenant le template avec les balises
    fichier_in = open("ifnti/liste_niveauElv.tex", 'r')
    #fichier en sortie accueillant les données fournies
    fichier_out = open("out/template_niv_out.tex", 'w')
    template = fichier_in.read() #lecture du template
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__)) + "/out/images/"
    
    j2_template = j2_env.from_string(template)
    # écriture dans le fichier en sortie
    fichier_out.write(j2_template.render(monContext))
    fichier_out.close()
    
    mon_pdf = build_pdf(open("out/template_niv_out.tex", 'r'))
    mon_pdf.save_to("out/liste_niveauElv.pdf")
    
    fichier_in.close()
    
    
def generate_note_pdf(context) :

    j2_env = Environment(
        variable_start_string="\VAR{",variable_end_string="}",
        block_start_string="\BLOCK{",block_end_string="}", 
        comment_start_string="\COMMENT{",comment_end_string="}"
        )
   
    #fichier à lire contenant le template avec les balises
    fichier_in = open("ifnti/notesEleves.tex", 'r')
    #fichier en sortie accueillant les données fournies
    fichier_out = open("out/template_note_out.tex", 'w')
    template = fichier_in.read() #lecture du template
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__)) + "/out/images/"
    
    j2_template = j2_env.from_string(template)
    # écriture dans le fichier en sortie
    fichier_out.write(j2_template.render(monContext))
    fichier_out.close()
    
    mon_pdf = build_pdf(open("out/template_note_out.tex", 'r'))
    mon_pdf.save_to("out/notesEleves.pdf")
    
    fichier_in.close()
    
# Dans ton fichier controleur.py ou un autre module

def generate_synthese_pdf(context):
    j2_env = Environment(
        variable_start_string="\VAR{",
        variable_end_string="}",
        block_start_string="\BLOCK{",
        block_end_string="}",
        comment_start_string="\COMMENT{",
        comment_end_string="}"
    )

    # Lire le template spécifique pour la synthèse
    fichier_in = open("ifnti/notesSyntheses.tex", 'r')
    fichier_out = open("out/template_synthese_out.tex", 'w')
    template = fichier_in.read()
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__)) + "/out/images/"

    j2_template = j2_env.from_string(template)
    fichier_out.write(j2_template.render(monContext))
    fichier_out.close()

    mon_pdf = build_pdf(open("out/template_synthese_out.tex", 'r'))
    mon_pdf.save_to("out/notesSyntheses.pdf")

    fichier_in.close()
    
    