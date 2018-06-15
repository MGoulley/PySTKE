import pke
import os
import sys

extractor = pke.unsupervised.TopicRank(input_file= sys.argv[1], language='french')

# load the content of the document, here document is expected to be in raw
# format (i.e. a simple text file) and preprocessing is carried out using nltk
extractor.read_document(format='raw', use_lemmas=False, stemmer='french')

# keyphrase candidate selection, in the case of TopicRank: sequences of nouns and adjectives
extractor.candidate_selection()

# candidate weighting, in the case of TopicRank: using a random walk algorithm
try:
    extractor.candidate_weighting(threshold=0.90)
    #extractor.grammar_selection(grammar=None)
    # N-best selection, keyphrases contains the 10 highest scored candidates as (keyphrase, score) tuples
    tuples = extractor.get_n_best(n=70, stemming=False)
    keyphrases = []
    for i in tuples:
        keyphrases.append(i[0])
except ValueError:
    pass



# Ecriture dans un fichier du resultat
base = os.path.basename(sys.argv[1])
filename = os.path.splitext(base)[0]
work_dir = os.getcwd() + "/corpus/"
addr = work_dir + filename + "_kw.txt"

file = open(addr,"wb")
try:
    for keyphrase in keyphrases:
        file.write(keyphrase.encode('utf-8') + b"\n")
except NameError:
    pass
file.close()
