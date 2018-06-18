from exide.parse import parse
import os
import sys

exide_presentation = parse(sys.argv[1])
i = 1
data = ""
entite_nommee = ""
emphasized = ""
while exide_presentation.get_slide_by_id(i) != None:
    data = data + exide_presentation.get_slide_by_id(i).text
    # Exploitable
    #print(exide_presentation.get_slide_by_id(i).title)
    # Pas terrible
    #print(exide_presentation.get_slide_by_id(i).urls)
    #print(exide_presentation.get_slide_by_id(i).named_entities)
    """
    Possibilite de poursuite :
    data = data + exide_presentation.get_slide_by_id(i).title

    for elt in exide_presentation.get_slide_by_id(i).urls:
        data = data + elt
    print(exide_presentation.get_slide_by_id(i).title)

    for elt in exide_presentation.get_slide_by_id(i).named_entities:
        entite_nommee = entite_nommee + elt.decode('cp1252').encode('utf-8') + "\n"
    for elt in exide_presentation.get_slide_by_id(i).emphasized_terms:
        emphasized = emphasized + elt
    for elt in exide_presentation.get_slide_by_id(i).named_entities:
        data = data + elt.encode('utf-8')
    for elt in exide_presentation.get_slide_by_id(i).emphasized_terms:
        data = data + elt.encode('ascii','ignore').strip()
    """
    i = i + 1

# Ecriture du resultat dans un fichier txt
base = os.path.basename(sys.argv[1])
work_dir = sys.argv[2]
filename = os.path.splitext(base)[0]
fichier = work_dir + filename + ".txt"
file = open(fichier,"w")
file.write(data.encode('utf-8'))
file.close()

"""
fichier = filename + "_entity.txt"
file = open(fichier,"w")
file.write(entite_nommee.encode('utf-8'))
file.close()

fichier = filename + "_emph.txt"
file = open(fichier,"w")
file.write(emphasized.encode('utf-8'))
file.close()
"""


# UTILISATION :
# python extract.py /home/matthias/CoursCOCO/CoursCOCO/CMCryptographie.pptx
