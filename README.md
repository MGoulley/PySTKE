# PySTKE
Python Slides and Transcriptions Keywords Extractor.
Outil d'extraction de mots clés dans des diaporamas et des transcriptions de la parole.

## Table des matières
* [Contenu du projet](#contenu-du-projet)
* [Pour commencer](#pour-commencer)
  - [Installation](#installation)
  - [Dependances](#dependances)
  - [Installer PKE](#installer-pke)
  - [Installer Exide](#installer-exide)
* [Les options de lancement](#les-options-de-lancement)
* [Les méthodes d'extractions](#les-methodes-d'extractions)
* [Effectuer les tests](#effectuer-les-tests)
* [Créer son extracteur de mots clés](#creer-son-extracteur-de-mots-cles)
* [Auteur](#auteur)
* [References](#references)

## Contenu du projet

- Le répertoire 'corpus' contient tous les fichiers que PySTKE produit lors de son exécution.
C'est dans ce répertoire que vous retrouverez le détail des mots clés annotés automatiquement.
- Le répertoire 'PASTEL' contient tous les fichiers d'exemple. (Supports de cours et transcriptions de la parole)
C'est aussi dans ce répertoire que vous trouverez mes annotations manuelles de ces supports de cours et transcriptions de la parole.
- Le répertoire 'Doc' contient mon rapport de stage et mon support de présentation qui vous apporteront des informations complémentaires.

## Pour commencer

Ces instructions vont vous permettre d'obtenir une copie du projet et de le lancer sur votre machine locale.
PySTKE nécessite Python2.7 ET Python3 d'installé sur votre machine pour fonctionner.

### Installation

Vous pouvez télécharger les sources du projet via GitHub (https://github.com/MGoulley/PySTKE) et l'installer ou bon vous semble sur votre machine.

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

Que vous pouvez installer avec :

```
sudo pip install openpyxl PyPDF2 nltk numpy pyrata scipy networkx sklearn unidecode future
sudo pip3 install openpyxl PyPDF2 nltk numpy pyrata scipy networkx sklearn unidecode future
```

Si vous avez un soucis d'installation avec pip, vous pouvez installer les dépendances avec :

```
sudo apt-get install python-openpyxl
sudo apt-get install python3-openpyxl
sudo apt-get install python-numpy
sudo apt-get install python-pypdf2
...
```

### Installer PKE
Il vous faudra installer PKE via la commande:
```
sudo pip install git+https://github.com/boudinfl/pke.git
```

### Installer Exide
Finalement, il faudra installer Exide :
```
sudo pip install git+https://github.com/Codophile1/exide
```

## Les options de lancement
Voici la liste des arguments disponibles au lancement de PySTKE.

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

## Les méthodes d'extractions
- PKE[pke] : Fonctionne avec la fréquence des mots dans le texte.
- PyRATA[pyrata] : Utilise des patrons syntaxique pour extraire des mots clés.
- Mixt[mixt] : Combine PKE et PyRATA.
- Wikifier[wikifier] : Utilise l'outil Wikifier (http://wikifier.org/) pour extraire des mots clés.

## Effectuer les tests

La commande suivante permet d'extraire les mots clés contenus dans un diaporama:
```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf
```
Par defaut, PySTKE utilise PyRATA pour extraire des mots clés.
Si vous souhaitez utiliser un autre outil, il faut utiliser l'option '-t' ou '--tool' :
```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -t wikifier
```
A l'aide de cette commande, on extrait des mots clés avec Wikifier.
Si l'on souhaite comparer une annotation automatique avec une annotation manuelle, il faut ajouter l'option '-r' ou '--ref' suivi du chemin vers le document contenant les mots clés relevés automatiquement. Cela nous produit alors un affichage de ce type :
```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -r PASTEL/annotation_manuelle/2014_Bourdon_Introduction_informatique.xlsx
Il y a 23 matchs, 280 erreurs, 23 approximations.
Nombre d'éléments annotés automatiquement : 287
Nombre d'éléments annotés manuellement : 83
Avec Approximation :
Precision: 0.160278745645 Rappel: 0.55421686747 F-Score: 0.248648648649
Sans Approximation :
Precision: 0.0801393728223 Rappel: 0.277108433735 F-Score: 0.124324324324
```
Vous pouvez remarquer que, ici, nous n'avons pas spécifier l'option '-t', nous avons donc extrait des mots clés avec l'outil PyRATA.

```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -r PASTEL/annotation_manuelle/2014_Bourdon_Introduction_informatique.xlsx -t pke --count
Il y a 13 matchs, 182 erreurs, 7 approximations.
Nombre d'éléments annotés automatiquement : 138
Nombre d'éléments annotés manuellement : 83
Avec Approximation :
Precision: 0.144927536232 Rappel: 0.240963855422 F-Score: 0.180995475113
Sans Approximation :
Precision: 0.0942028985507 Rappel: 0.156626506024 F-Score: 0.117647058824
Il y a dans ce document 3201 mots.
Vous avez annoté manuellement 164 mots.
Cela représente 5.123398937831928%% de mots annotés.
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

## Auteur

* **Matthias Goulley** - Contact : mattgoulley@gmail.com
Pour obtenir des informations complémentaires, vous pouvez consulter mon rapport de stage et mon support de présentation situés dans le répertoire '/doc'.

## References

Je remercie ces outils qui m'ont aidés pour ce projet.

### Exide
https://github.com/Codophile1/exide

### Python Keyphrase Extractor
https://github.com/boudinfl/pke (Florian Boudin)

### Python Rule-based feAture sTructure Analysis
https://github.com/nicolashernandez/PyRATA (Nicolas Hernandez)
