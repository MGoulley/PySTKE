# coding: utf8

import urllib.parse, urllib.request, json
import os
import sys

MAX_CHAR = 10000

def CallWikifier(text, lang="fr", threshold=0.8):
    # Prepare the URL.
    data = urllib.parse.urlencode([
        ("text", text), ("lang", lang),
        ("userKey", "mqqmzpabglxubvfhgnyppnupsozklf"),
        ("pageRankSqThreshold", "%g" % threshold), ("applyPageRankSqThreshold", "true"),
        ("nTopDfValuesToIgnore", "200"),
        ("wikiDataClasses", "true"), ("wikiDataClassIds", "false"),
        ("support", "true"), ("ranges", "false"),
        ("includeCosines", "false"), ("maxMentionEntropy", "3")
        ])
    url = "http://www.wikifier.org/annotate-article"
    # Call the Wikifier and read the response.
    req = urllib.request.Request(url, data=data.encode("utf8"), method="POST")
    with urllib.request.urlopen(req, timeout = 60) as f:
        response = f.read()
        response = json.loads(response.decode("utf-8"), strict=False)
    # Output the annotations.
    annot = []
    for annotation in response["annotations"]:
        keyword = annotation["title"]
        if keyword not in annot:
            annot.append(keyword)
        #print("%s (%s)" % (annotation["title"], annotation["url"]))
    return annot

with open(sys.argv[1], "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip())

text_acc = ""
request_size = 0
result = []
for element in array:
    if len(element) + request_size > MAX_CHAR:
        result.append(CallWikifier(text_acc.encode("utf8")))
        text_acc = element
        request_size = len(element)
    else:
        text_acc = text_acc + element
        request_size = request_size + len(element)

# Ecriture dans un fichier du resultat
base = os.path.basename(sys.argv[1])
filename = os.path.splitext(base)[0]
work_dir = os.getcwd() + "/corpus/"
addr = work_dir + filename + "_kw.txt"

file = open(addr,"wb")
try:
    for table in result:
        for keyphrase in table:
            file.write(keyphrase.encode('utf-8') + b"\n")
except NameError:
    pass
file.close()
