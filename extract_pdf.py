# coding: utf-8

import sys
import os
import re

dir = sys.argv[1]
base = os.path.basename(dir)
filename = os.path.splitext(base)[0]
extension = os.path.splitext(base)[1]
output = sys.argv[2] + filename + ".txt"
# -sort -ignoreBeads
cmd = "java -jar pdfbox-app-2.0.9.jar ExtractText -encoding utf-8 " + dir + " " + output
os.system( cmd + " > /dev/null 2>&1")

"""
file = open(output,"r")
lst = list(file)
file.close()
file = open(output,"w")
text = ""
for elt in lst:
    #elt = re.sub(r'[^\x00-\x7f]',r'', elt)
    #elt = elt.decode('utf-8','ignore').encode("utf-8")
    #elt = bytes(elt, 'utf-8').decode('utf-8', errors='replace')
    #elt = elt.decode("utf-8", errors='strict')
    #elt = re.sub(r'[^\w|\s|’]', '', elt)
    file.write(elt.decode('utf-8', errors='replace').encode('utf-8') + b'\n')
file.close()
"""
