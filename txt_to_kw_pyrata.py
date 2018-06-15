import pyrata.re as pyrata_re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import StanfordPOSTagger
import sys
import os
import re

jar = '/home/matthias/pyKE/stanford-postagger-full-2018-02-27/stanford-postagger-3.9.1.jar'
model = '/home/matthias/pyKE/stanford-postagger-full-2018-02-27/models/french.tagger'
#java_path = "export JAVA_HOME=/usr/lib/jvm/java-9-openjdk-amd64"
#os.environ['JAVAHOME'] = java_path
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def Handel_simpleNP_Penn(data):
    pattern = '(pos="JJ"|pos="NN")* pos="NN" (pos="IN" pos="DT"* (pos="JJ"|pos="NN")* pos="NN")*'
    pattern = '(pos~"JJ|JJR|JJS" pos~"NN|NNS|NNP|NNPS")* pos~"NN|NNS|NNP|NNPS" (pos="IN" pos="DT"* (pos~"JJ|JJR|JJS"|pos~"NN|NNS|NNP|NNPS")* pos~"NN|NNS|NNP|NNPS")*'
    return pyrata_re.findall(pattern, data)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def Handel_FullNP_multi_tag_set(data):
    data = pyrata_re.update('pos~"JJ|JJR|JJS|CD|ADJ|A"', {'pos':"Adj1"}, data)  # ADJ
    data = pyrata_re.update('pos~"DT|DET|D"', {'pos':"Det1"}, data)           # DET
    data = pyrata_re.update('pos~"IN|TO|ADP|P"', {'pos':"Prep1"}, data)         # ADP
    data = pyrata_re.update('pos~"RB|RBR|RBS|ADV|R"', {'pos':"Adv1"}, data)     # ADV
    data = pyrata_re.update('pos~"Adv1|RP|MD|PRT|V"', {'pos':"VerbMod1"}, data) # VERB
    data = pyrata_re.update('pos~"NN|NNS|NNP|NNPS|FW|CD|NOUN|NUM|^|N"', {'pos':"Noun"}, data) # NOUN
    data = pyrata_re.update('pos~"VB|VBD|VBG|VBN|VBP|VBZ|VERB"', {'pos':"Verb"}, data) # VERB
    #data = pyrata_re.update('pos~"O|Adj1|Det1|Prep1|Adv1|VerbMod1|Noun|Verb|CoarseDOT|CoarseADJ|CoarseADP|CoarseADV|CoarseCONJ|CoarseDET|CoarseNOUN|CoarseNUM|CoarsePRON|CoarsePRT|CoarseVERB|CoarseX"', {'pos':"AnyPOS"}, data)
    data = pyrata_re.update('pos~"-LRB-|-LSB-|-LCB-"', {'pos':"Lparen"}, data)
    data = pyrata_re.update('pos~"-RRB-|-RSB-|-RCB-"', {'pos':"Rparen"}, data)

    # for each transducer level increment the chk indice (chk stands for chunk)
    data = pyrata_re.extend('pos="Adj1" (pos="CC" pos="Adj1")*', {'chk1':"Adj"}, data, iob = True)
    data = pyrata_re.extend('pos="Det1" (pos="CC" pos="Det1")*', {'chk1':"Det"}, data, iob = True)
    data = pyrata_re.extend('pos="Adv1" (pos="CC" pos="Adv1")*', {'chk1':"Adv"}, data, iob = True)
    data = pyrata_re.extend('pos="Prep1" (pos="CC" pos="Prep1")*', {'chk1':"Prep"}, data, iob = True)
    data = pyrata_re.extend('pos="VerbMod1" (pos="CC" pos="VerbMod1")*', {'chk1':"VerbMod"}, data, iob = True)
    data = pyrata_re.extend('(chk1-"Adj" | pos="Noun")*', {'chk2':"BaseNP"}, data, iob = True)
    data = pyrata_re.extend('chk1-"Prep" (chk1-"Det" | chk1-"Adj")* chk2-"BaseNP"', {'chk3':"PP"}, data, iob = True)
    data = pyrata_re.extend('pos="Lparen" .+ pos="Rparen"', {'chk4':"ParenP"}, data, iob = True)
    data = pyrata_re.extend('chk2-"BaseNP" (chk3-"PP" | chk4-"ParenP")*', {'chk5':"NP1"}, data, iob = True)
    data = pyrata_re.extend('chk5-"NP1" (pos="CC" (chk1-"Det" | chk1-"Adj")* chk5-"NP1")*', {'chk6':"NP"}, data, iob = True)
    return pyrata_re.findall('chk6-"NP"' , data)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def JK_extendedNP_Penn(data):
    pattern = '((pos="JJ"|pos="NN")+ | (((pos="JJ"|pos="NN")* (pos="NN" pos="IN")? (pos="JJ"|pos="NN")*)) pos="NN"'
    return pyrata_re.findall(pattern, data)


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def JK_simpleNP_Penn(data):
    patterns = set(['pos="JJ" pos="NN"',
    'pos="NN" pos="NN"',
    'pos="JJ" pos="JJ" pos="NN"',
    'pos="JJ" pos="NN" pos="NN"',
    'pos="NN" pos="JJ" pos="NN"',
    'pos="NN" pos="NN" pos="NN"',
    'pos="NN" pos="IN" pos="NN"'])

    noun_phrases = []
    for p in patterns:
        noun_phrases.extend(pyrata_re.findall(p, data))
    return noun_phrases



file = open(sys.argv[1],"r")
text=file.read().replace('\n', ' ')
file.close()
"""
# Lecture des entités nommées :
addr = filename + "_entity.txt"
file = open(addr,"r")
entity = file.readlines()
file.close()
# Lecture des emphasized :
addr = filename + "_emph.txt"
file = open(addr,"r")
emph = file.readlines()
file.close()
"""
data =  [{'raw':word, 'pos':pos} for (word, pos) in nltk.pos_tag(nltk.word_tokenize(text))]

#result = JK_simpleNP_Penn(data)
#result = Handel_simpleNP_Penn(data)
result = JK_extendedNP_Penn(data)
#result = Handel_FullNP_multi_tag_set(data)

if result != None:
    prekeyphrases = []
    stop_words = set(stopwords.words('french'))
    additional_sw = ['oui', 'non', 'etc', 'celle', 'dont', 'ceux', 'si', 'là','ex', 'vs', 'dès', '|', '||', "'", "les"]
    stop_words = stop_words.union(additional_sw)

    for i in range(len(result)):
        acc = ""
        for j in range(len(result[i])):
            acc += result[i][j]["raw"] + " "
        #print("PyRATA : " + acc)
        acc = re.sub(r'[^(\w|\s|\-)]', '', acc)
        #print("Sup des symboles : " + acc)
        acc = re.sub(r'(^((' + "|".join(stop_words) + r')\s)*)', '', acc, re.IGNORECASE) # Suppression des stopwords en debut d'expression
        #print("Sup stopwords first : " + acc)
        acc = re.sub(r'((\s( ' + '|'.join(stop_words) + r'))+.$)', '', acc, re.IGNORECASE) # Suppression des stopwords en fin d'expression
        #print("Sup stopwords fin : " + acc)
        acc = re.sub(r'^\s?(\b\w{1}\s)*', '', acc) # Suppression des mot d'une seule lettre
        acc = re.sub(r'^\w{1}\b', '', acc)
        #print("Expression annotée : " + acc)
        if (acc.rstrip() not in prekeyphrases) and (acc.rstrip() != '') and (acc.rstrip() != ' '):
            prekeyphrases.append(acc.rstrip())

    """
    entitys = []
    for elt in entity:
        elt = elt.rstrip()
        elt = elt.lower()
        #print("ELT deb :" + elt + ":")
        elt = re.sub(r'[^(\w|\s|\-)]', '', elt)
        elt = re.sub(r'(^((' + '|'.join(stop_words) + r')(\s|$))*)', '', elt, re.IGNORECASE) # Suppression des stopwords en debut d'expression
        elt = re.sub(r'((\s( ' + '|'.join(stop_words) + r'))+.$)', '', elt, re.IGNORECASE) # Suppression des stopwords en fin d'expression
        elt = re.sub(r'^\s?(\b\w{1}\s)*', '', elt) # Suppression des mot d'une seule lettre
        elt = re.sub(r'^\w{1}\b', '', elt)
        #print("ELT fin :" + elt + ":")
        if (elt not in entitys) and (elt != '') and (elt != ' '):
            entitys.append(elt)

    entitys_keyphrases = []
    for elt in entitys:
        res = pos_tagger.tag(elt.split())
        print(res)
        #if len(res) == 1:
        #    if ((res[0][1] == 'N') or (res[0][1] == 'NC')):
        #        keyphrases.append(prekp)
        #else:
        #    keyphrases.append(prekp)
    """


    keyphrases = []
    for prekp in prekeyphrases:
        res = pos_tagger.tag(prekp.split())
        if len(res) == 1:
            if ((res[0][1] == 'N') or (res[0][1] == 'NC')):
                keyphrases.append(prekp)
        else:
            keyphrases.append(prekp)

    # Ecriture dans un fichier du resultat
    base = os.path.basename(sys.argv[1])
    filename = os.path.splitext(base)[0]
    work_dir = os.getcwd() + "/corpus/"
    addr = work_dir + filename + "_kw.txt"

    file = open(addr,"wb")
    try:
        for keyphrase in keyphrases:
            file.write(keyphrase.encode('utf-8')+ b"\n")
    except NameError:
        pass
    file.close()

else:
    # Ecriture dans un fichier du resultat
    base = os.path.basename(sys.argv[1])
    filename = os.path.splitext(base)[0]
    work_dir = os.getcwd() + "/corpus/"
    addr = work_dir + filename + "_kw.txt"
    file = open(addr,"wb")
    file.close()
