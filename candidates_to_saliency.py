import pke
import sys
import os

# initialize TfIdf model
extractor = pke.unsupervised.TfIdf(input_file=sys.argv[1])

# load the DF counts from file
df_counts = pke.load_document_frequency_file(input_file=sys.argv[2])

# load the content of the document
extractor.read_document(format='raw')

# keyphrase candidate selection
extractor.candidate_selection()

# candidate weighting with the provided DF counts
extractor.candidate_weighting(df=df_counts)

# N-best selection, keyphrases contains the 10 highest scored candidates as
# (keyphrase, score) tuples
keyphrases = extractor.weights

base = os.path.basename(sys.argv[1])
filename = os.path.splitext(base)[0]

file = open(os.getcwd() + "/corpus/" + filename + "_saliency.txt","wb")
try:
    for k, v in keyphrases.iteritems():
        file.write(k.encode('utf-8') + '  ' + str(v).encode('utf-8') + b"\n")
except NameError:
    pass
file.close()


# UTILISATION
# python candidates_to_saliency.py corpus/2014_Bourdon_Introduction_informatique.txt corpus/2014_Bourdon_Introduction_informatique_frequency.gz
