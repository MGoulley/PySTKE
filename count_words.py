import os
import re
import nltk
import sys

fichier = sys.argv[1]
if os.path.isfile(fichier):
    file = open(fichier,"r", encoding = "ISO-8859-1")
    data = list(file)
    nb_words = 0
    for elt in data:
        elt = elt.rstrip()
        elt = re.sub(r'.*> ', '', elt)
        sentence = elt.split()
        nb_words = nb_words + len(sentence)
    print(nb_words)
    file.close()


# UTILISATION :
# python3 count_words.py /home/matthias/rapportstage/annotations/20131010.stm
