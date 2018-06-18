# coding: utf-8

import sys
import os
import re

dir = sys.argv[1]
base = os.path.basename(dir)
filename = os.path.splitext(base)[0]
extension = os.path.splitext(base)[1]
output = sys.argv[2] + filename + ".txt"
cmd = "java -jar pdfbox-app-2.0.9.jar ExtractText -encoding utf-8 " + dir + " " + output
os.system( cmd + " > /dev/null 2>&1")
