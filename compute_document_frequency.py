from pke import compute_document_frequency
from string import punctuation
import sys
import os

# path to the collection of documents
input_dir = sys.argv[1]

# path to the DF counts dictionary, saved as a gzip tab separated values
output_file = sys.argv[2]

# compute df counts and store stem -> weight values
compute_document_frequency(input_dir=input_dir,
                           output_file=output_file,
                           format="raw",            # input files format
                           use_lemmas=False,    # do not use Stanford lemmas
                           stemmer=None,            # use porter stemmer
                           stoplist=list(punctuation),            # stoplist
                           delimiter='\t',            # tab separated output
                           extension='txt',          # input files extension
                           n=5)              # compute n-grams up to 5-grams

# UTILISATION
# python compute_document_frequency.py corpus/ corpus/2014_Bourdon_Introduction_informatique_frequency.gz
