# PySTKE
Python Slides and Transcriptions Keywords Extractor.
Outil d'extraction de mots clés dans des diaporamas et des transcriptions de la parole.
Formats supportés pour les diaporamas et transcriptions :
- .pptx
- .tex
- .odp
- .stm
- .txt

## Table des matières
* [Contenu du projet](#contenu-du-projet)
* [Pour commencer](#pour-commencer)
  - [Installation](#installation)
  - [Dependances](#dependances)
  - [Installer PKE](#installer-pke)
  - [Installer Exide](#installer-exide)
* [Les options de lancement](#les-options-de-lancement)
* [Les méthodes d'extractions](#les-méthodes-d'extractions)
* [Effectuer les tests](#effectuer-les-tests)
* [Créer son extracteur de mots clés](#créer-son-extracteur-de-mots-clés)
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
Il faudra aussi installer Exide :
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
Le document '-d' doit être au format:
- .pptx, .tex ou .odp pour un diaporama
- .txt ou .stm pour une transcription de la parole
Le document '-r' doit être au format .xlsx.

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
#Extraction à l'aide de PKE :
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -t pke
#Extraction à l'aide de PyRATA :
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -t pyrata
#Extraction à l'aide de Mixt :
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -t mixt
#Extraction à l'aide de Wikifier :
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -t wikifier
```
Si l'on souhaite comparer une annotation automatique avec une annotation manuelle, il faut ajouter l'option '-r' ou '--ref' suivi du chemin vers le document contenant les mots clés relevés automatiquement (format .xlsx). Cela nous produit alors un affichage de ce type :
```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -r PASTEL/annotation_manuelle/2014_Bourdon_Introduction_informatique.xlsx
Nombre d'éléments annotés manuellement : 83
Nombre d'éléments annotés automatiquement : 287
Il y a 23 matchs, 280 erreurs, 23 approximations.
Méthode de résolution & Précision & Rappel & F-Score //
Avec Approximation & 0.160 & 0.554 & 0.249 //
Sans Approximation & 0.080 & 0.277 & 0.124 //
```
Vous pouvez remarquer que, ici, nous n'avons pas spécifier l'option '-t', nous avons donc extrait des mots clés avec l'outil PyRATA.
Si je souhaite avoir plus de détail sur mon annotation manuelle, je peux utiliser '--count'
```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -r PASTEL/annotation_manuelle/2014_Bourdon_Introduction_informatique.xlsx --count
Nombre d'éléments annotés manuellement : 83
Nombre d'éléments annotés automatiquement : 287
Il y a 23 matchs, 280 erreurs, 23 approximations.
Méthode de résolution & Précision & Rappel & F-Score //
Avec Approximation & 0.160 & 0.554 & 0.249 //
Sans Approximation & 0.080 & 0.277 & 0.124 //
Il y a dans ce document 3201 mots.
Vous avez annoté manuellement 164 mots.
Cela représente 5.123%% de mots annotés.
```
Par defaut, PySTKE compare le fichier d'annotation automatique et le fichier d'annotation manuelle par mots clés par diapositive.
Si on veut les comparer par l'ensemble des mots clés unique dans les deux fichiers, il faut utiliser l'option '--unique'.
```
~/PySTKE$ python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_informatique.pdf -r PASTEL/annotation_manuelle/2014_Bourdon_Introduction_informatique.xlsx --unique
Nombre d'éléments annotés manuellement : 57
Nombre d'éléments annotés automatiquement : 81
Il y a 13 matchs, 82 erreurs, 20 approximations.
Méthode de résolution & Précision & Rappel & F-Score //
Avec Approximation & 0.407 & 0.579 & 0.478 //
Sans Approximation & 0.160 & 0.228 & 0.188 //
```

Pour les transcriptions, on peut utiliser les mêmes options que précédemment. Par exemple, pour extraire les mots clés d'une transcription avec l'outil 'mixt', on utilise la commande :
```
python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_algorithmique.stm -t mixt
```
Pour les transcriptions, il n'est pour l'instant pas possible de les comparer par diapositive, on est alors obligé d'utiliser le mot clé '--unique' pour comparer une annotation automatique d'une transcription avec l'annotation manuelle.
```
python3 main.py -d PASTEL/supports/2014_Bourdon_Introduction_algorithmique.stm -r PASTEL/annotation_manuelle/2014_Bourdon_Introduction_algorithmique_transcription.xlsx -t pke --unique
Nombre d'éléments annotés manuellement : 26
Nombre d'éléments annotés automatiquement : 70
Il y a 2 matchs, 80 erreurs, 7 approximations.
Méthode de résolution & Précision & Rappel & F-Score //
Avec Approximation & 0.129 & 0.346 & 0.187 //
Sans Approximation & 0.029 & 0.077 & 0.042 //
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

Voici un template de ce fichier :
```python
import os
import sys

def save_keywords_to_file(keywords_table):
    # Write keywords line by line in txt file
    base = os.path.basename(path_to_raw_text_file)
    filename = os.path.splitext(base)[0]
    work_dir = os.getcwd() + "/corpus/"
    keywords_file_path = work_dir + filename + "_kw.txt"

    file = open(keywords_file_path,"wb")
    try:
        for keyword in keywords_table:
            file.write(keyword.encode('utf-8') + b"\n")
    except NameError:
        pass
    file.close()

# The first arg is a path to the extracted raw text file from the source or the PDF
path_to_raw_text_file = sys.argv[1]

# some stuff
# which extract
# keywords ...

# store all the extacted keywords by passing a table wich contain all extracted keywords
save_keywords_to_file(keywords_table)
```
Vous récupérez en premier argument (sys.argv[1]) le chemin vers le fichier texte à étudier pour extraire les mots clés.
Vous pouvez ensuite appliquer nimporte quelle méthode pour extraire les mots clés.
Pour finir, la fonction 'save_keywords_to_file()' permet d'enregistrer un fichier résultat contenant vos mots clés extraits avec par votre méthode à partir d'un tableau de mots clés donné en paramètre.

## Annotation manuelle

Un fichier d'annotation manuelle se présente toujours sous la forme d'un tableur composé de deux colonnes.
La première contient le numéro de la diapositive et la seconde contient le mot clé relevé par l'annotateur sur la diapositive.

| Numéro Diapositive    | Mot clé |
| ---                   | ---       |
| 1                     | Informatique |
| 1                     | Algorithme        |
| 2                     | Variable       |
| 3                     | Algorithme       |

Vous pouvez trouver des exemples de ces fichiers dans le répertoire '~/PySTKE/PASTEL/annotation_manuelle/'.

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
