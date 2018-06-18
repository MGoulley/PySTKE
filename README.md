# PySTKE

Outil d'extraction de mots clés dans des diaporamas et des transcriptions de la parole.

## Pour commencer

Ces instructions vont vous permettre d'obtenir une copie du projet et de le lancer sur votre machine locale.

### Installation

Vous pouvez télécharger les sources du projet via GitHub et l'installer ou bon vous semble sur votre machine.

### Dependances

Ce projet requiert les dépendances suivantes :

```
openpyxl 2.5.3 https://openpyxl.readthedocs.io/en/stable/
PyPDF2 1.26.0 https://pythonhosted.org/PyPDF2/
pke https://github.com/boudinfl/pke
nltk https://www.nltk.org/install.html
numpy https://www.nltk.org/install.html
exide https://github.com/Codophile1/exide
pyrata https://github.com/nicolashernandez/PyRATA
scipy https://www.scipy.org/install.html
networkx https://networkx.github.io/documentation/stable/install.html
sklearn http://scikit-learn.org/stable/install.html
unidecode https://pypi.org/project/Unidecode/
future http://python-future.org/quickstart.html
```

### Les options de lancement

```
usage: main.py [-h] [-d DOC] [-t [TOOL]] [-r [REF]] [--unique [UNIQUE]] [--count [COUNT]]

Extracteur automatique de mots clés

optional arguments:
  -h, --help            show this help message and exit
  -d DOC, --doc DOC     Chemin vers le document à annoter automatiquement
  -t [TOOL], --tool [TOOL] Outil à utiliser pour extraire les mots clés: pke, pyrata, mixt, wikifier (defaut pyrata)
  -r [REF], --ref [REF] Chemin vers le document d'annotation manuelle à comparer avec l'extraction automatique
  --unique [UNIQUE]     Compare par mots clés uniques dans le document. (Par diapositive par default)
  --count [COUNT]       Ajoute des détails sur les expressions annotées manuellement
```

### Effectuer les tests

Vous pouvez exécuter les commandes suivantes pour tester le programme :

```
*** Introduction à l'informatique ***
python3 main.py -d ~/PySTKE/PASTEL/diaporama/info.pdf -r ~/PySTKE/PASTEL/annotation_manuelle_diaporama/info.xlsx -t pke --count
python3 main.py -d ~/PySTKE/PASTEL/diaporama/info.pdf -r ~/PySTKE/PASTEL/annotation_manuelle_diaporama/info.xlsx -t pke --unique
python3 main.py -d ~/PySTKE/PASTEL/transcription/20140911.stm -r ~/PySTKE/PASTEL/annotation_manuelle_transcription/info.xlsx -t pke --count --unique

*** Introduction à l'algorithmique ***
python3 main.py -d ~/PySTKE/PASTEL/diaporama/algo.pdf -r ~/PySTKE/PASTEL/annotation_manuelle_diaporama/algo.xlsx -t pke --count
python3 main.py -d ~/PySTKE/PASTEL/diaporama/algo.pdf -r ~/PySTKE/PASTEL/annotation_manuelle_diaporama/algo.xlsx -t pke --unique
python3 main.py -d ~/PySTKE/PASTEL/transcription/20140912.stm -r ~/PySTKE/PASTEL/annotation_manuelle_transcription/algo.xlsx -t pke --count --unique

*** Les Fonctions dans l'algorithmique ***
python3 main.py -d ~/PySTKE/PASTEL/diaporama/fonct.pdf -r ~/PySTKE/PASTEL/annotation_manuelle_diaporama/fonct.xlsx -t pke --count
python3 main.py -d ~/PySTKE/PASTEL/diaporama/fonct.pdf -r ~/PySTKE/PASTEL/annotation_manuelle_diaporama/fonct.xlsx -t pke --unique
```

## Créer son extracteur de mots clés
Vous pouvez créer votre propre extracteur de mots clés utilisable avec cet outil. Il suffit de créer un fichier Python dans le dossier comportant le programme principal, avec ce nom :
```
txt_to_kw_XXX.py
```
Ou XXX est le nom de votre outil d'extraction de mots clés. Vous pouvez ensuite l'utiliser avec la commande :
```
python3 main.py -d directory/file.pdf -t XXX
```

## Author

* **Matthias Goulley** - Contact : mattgoulley@gmail.com

## References

Je remercie ces outils qui m'ont aidés pour ce projet.

### Exide
https://github.com/Codophile1/exide

### Python Keyphrase Extractor
https://github.com/boudinfl/pke (Florian Boudin)

### Python Rule-based feAture sTructure Analysis
https://github.com/nicolashernandez/PyRATA (Nicolas Hernandez)
