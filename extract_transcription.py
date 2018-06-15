import os
import re
import nltk
import sys

fichier = sys.argv[1]
base = os.path.basename(fichier)
filename = os.path.splitext(base)[0]
work_dir = os.getcwd() + "/corpus/"
addr = work_dir + filename + ".txt"
if os.path.isfile(fichier):
    file = open(fichier,"r", encoding = "ISO-8859-1")
    file2 = open(addr,"wb")
    data = list(file)
    nb_words = 0
    for elt in data:
        elt = elt.rstrip()
        elt = re.sub(r'.*> ', '', elt)
        file2.write(elt.encode('utf-8') + b"\n")
    file.close()
    file2.close()

# UTILISATION :
# python3 count_words.py /home/matthias/rapportstage/annotations/20131010.stm
