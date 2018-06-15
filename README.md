# PyKE

Outil d'extraction de mots clés à partir de diaporama et de transcription de la parole.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Dependances

Il vous faudra installer via PiP3 les dependances suivantes :

```
openpyxl
PyPDF2
pke
nltk
numpy
exide
pyrata
scipy
networkx
sklearn
unidecode
future
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

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

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
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
## Deployment

Add additional notes about how to deploy this on a live system

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.



