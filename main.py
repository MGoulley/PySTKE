#!/usr/bin/python3
#encoding: utf-8

import os
import sys
import os.path
import argparse
import re
import nltk
from openpyxl import Workbook
from openpyxl import load_workbook

# Fonctions
def CountWords(file):
    fichier = file
    base = os.path.basename(fichier)
    extension = os.path.splitext(base)[1]
    if os.path.isfile(fichier):
        file = open(fichier,"r", encoding = "ISO-8859-1")
        data = list(file)
        nb_words = 0
        for elt in data:
            elt = elt.rstrip()
            elt = re.sub(r'.*> ', '', elt)
            sentence = elt.split()
            nb_words = nb_words + len(sentence)
        print("Il y a dans ce document " + str(nb_words) + " mots.")
        file.close()
    return nb_words

def CountWordsInExcel(file):
    wb = load_workbook(filename=file, read_only=True)
    ws = wb.active
    nb_words = 0
    i=0
    rows = list(ws.rows)
    while (i < ws.max_row) and (rows[i][0].value != None):
        elt = rows[i][1].value.rstrip().lower()
        sentence = elt.split()
        nb_words = nb_words + len(sentence)
        i = i + 1
    print("Vous avez annoté manuellement " + str(nb_words) + " mots.")
    return nb_words

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def Extraction_keywords(tol, wrkdir, filnam):
    if(tol == 'pke'):
        os.system('python3 txt_to_kw_pke.py ' + wrkdir + filnam + ".txt")
    elif(tol == 'pyrata'):
        os.system('python3 txt_to_kw_pyrata.py ' + wrkdir + filnam + ".txt")
    elif(tol == 'mixt'):
        os.system('python3 txt_to_kw_mixt.py ' + wrkdir + filnam + ".txt")
    elif(tol == 'wikifier'):
        os.system('python3 txt_to_kw_wikifier.py ' + wrkdir + filnam + ".txt")
    elif os.path.isfile('txt_to_kw_' + dir + '.py'):
        os.system('python3 txt_to_kw_' + dir + '.py ' + wrkdir + filnam + ".txt")
    else:
        sys.exit("L'outil " + tol + " n'existe pas.")

def Comparaison_diapositive(file_ref, file_comp):
    if os.path.isfile(file_ref) and os.path.isfile(file_comp):
        base_ref = os.path.basename(file_ref)
        extension_ref = os.path.splitext(base_ref)[1]
        if(extension_ref == '.xlsx'):
            os.system('python excel_comp.py '+ file_ref +' ' + file_comp)
        else:
            sys.exit("L'extension du fichier " + file_ref + " n'est pas conforme.")
    else:
        sys.exit("Le fichier " + file_ref + " n'existe pas.")

def Comparaison_unique(file_ref, file_comp):
    work_dir = os.getcwd() + "/corpus/"
    if os.path.isfile(file_ref):
        base_ref = os.path.basename(file_ref)
        filename_ref = os.path.splitext(base_ref)[0]
        extension_ref = os.path.splitext(base_ref)[1]
        if(extension_ref == '.xlsx'):
            os.system('python excel_to_unique_keywords.py '+ file_ref + ' _unique_ref.xlsx')
        else:
            sys.exit("L'extension du fichier " + file_ref + " n'est pas conforme.")
    else:
        sys.exit("Le fichier " + file_ref + " n'existe pas.")
    if os.path.isfile(file_comp):
        base_comp = os.path.basename(file_comp)
        filename_comp = os.path.splitext(base_comp)[0]
        extension_comp = os.path.splitext(base_comp)[1]
        if(extension_comp == '.xlsx'):
            os.system('python excel_to_unique_keywords.py '+ file_comp + ' _unique_comp.xlsx')
        else:
            sys.exit("L'extension du fichier " + file_comp + " n'est pas conforme.")
    else:
        sys.exit("Le fichier " + file_comp + " n'existe pas.")
    Comparaison_diapositive(work_dir + filename_ref +'_unique_ref.xlsx', work_dir + filename_comp + '_unique_comp.xlsx')

# Analyse des arguments de lancement
parser = argparse.ArgumentParser(description='Extracteur automatique de mots clés')
parser.add_argument('-d', '--doc',  help='Chemin vers le document à annoter automatiquement')
parser.add_argument('-t', '--tool', nargs='?', default='pyrata', help='Outil à utiliser pour extraire les mots clés: pke, pyrata, mixt, wikifier (default pyrata)')
parser.add_argument('-r', '--ref', nargs='?', help='Chemin vers le document d\'annotation manuelle à comparer avec l\'extraction automatique')
parser.add_argument("--unique", type=str2bool, nargs='?', const=True, default=False, help="Comparaison par mots clés uniques dans le document. (Defaut : Par diapositive)")
parser.add_argument("--count", type=str2bool, nargs='?', const=True, default=False, help="Ajoute des détails sur les expressions annotées manuellement")

args = parser.parse_args()
dir = args.doc
file_ref = args.ref
tool = args.tool
unique = args.unique
count = args.count

# Constantes
exide_support = ['.pptx', '.odp', '.tex'] # .ppt ?
transcription_support = ['.stm', '.txt']

# Début du programme
if dir != None:
    work_dir = os.getcwd() + "/corpus/" # On stockera tous les fichiers produits dans un repertoire corpus
    base = os.path.basename(dir)
    filename = os.path.splitext(base)[0]
    extension = os.path.splitext(base)[1]
    if os.path.isfile(dir):
        if extension in exide_support: # Cas d'un fichier source
            # Step 1 : Extraction du texte
            os.system('python extract_src.py ' + dir + " " + work_dir)
            # Step 2 : Extraction des mots clés
            Extraction_keywords(tool, work_dir, filename)
            # Step 3 : Alignement des mots clés par diapositive
            os.system('python src_kw_export_excel.py ' + work_dir + filename + "_kw.txt " + dir)
        elif(extension == '.pdf'): # Cas d'un fichier PDF
            # Step 1 : Extraction du texte
            os.system('python extract_pdf.py ' + dir + " " + work_dir)
            # Step 2 : Extraction des mots clés
            Extraction_keywords(tool, work_dir, filename)
            # Step 3 : Alignement des mots clés par diapositive
            os.system('python3 pdf_kw_export_excel.py ' + work_dir + filename + "_kw.txt " + dir)
        elif extension in transcription_support: # Cas d'une Transcription
            # Step 1 : Extraction du texte
            os.system('python3 extract_transcription.py ' + dir + " " + work_dir)
            # Step 2 : Extraction des mots clés
            Extraction_keywords(tool, work_dir, filename)
            # Step 3 : Alignement des mots clés
            os.system('python3 transcription_kw_export_excel.py ' + work_dir + filename + "_kw.txt " + dir)
        else:
            sys.exit("L'extension du fichier " + dir + " n'est pas conforme.")
    else:
        sys.exit("Le fichier " + dir + " n'existe pas.")
    # Step 4 : Comparaison des résultats avec la ref dans un tableur
    if file_ref != None:
        if unique == True:
            Comparaison_unique(file_ref, work_dir + filename + '.xlsx')
        else:
            Comparaison_diapositive(file_ref, work_dir + filename + '.xlsx')
    # Step 5 : Résultats complémentaires annotation manuelle
    if count == True:
        file = work_dir + filename + ".txt"
        words_count = CountWords(file)
        if file_ref != None:
            words_annotate = CountWordsInExcel(file_ref)
            result = (words_annotate * 100)/words_count
            print("Cela représente " + str(result) + "%% de mots annotés.")
else:
    print("Vous n'avez pas spécifier de fichier à analyser.")


# UTILISATION
# python3 main.py -d /home/matthias/PASTEL/diapo_pastel/info.pdf -r /home/matthias/PASTEL/annot_diapo/info.xlsx -t pke
# python3 main.py -d /home/matthias/PASTEL/diaporama/reseaux2012.pptx -r /home/matthias/PASTEL/annotation_manuelle_diaporama/reseaux2012.xlsx -t pke
# python3 main.py -d /home/matthias/PASTEL/transcription/20140911.stm -r /home/matthias/PASTEL/annotation_manuelle_transcription/info.xlsx -t pke
# python3 main.py -d /home/matthias/PySTKE/PASTEL/diaporama/info.pdf -r /home/matthias/PySTKE/PASTEL/annotation_manuelle_diaporama/info.xlsx -t pke
# python3 main.py -d /home/matthias/PySTKE/PASTEL/diaporama/reseaux2012.pptx -r /home/matthias/PySTKE/PASTEL/annotation_manuelle_diaporama/reseaux2012.xlsx -t pke
