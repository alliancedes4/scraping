# OPENCLASSROOMS - Développeur d'application Python

## PROJET 2 SCRAPING

Ce projet Python consiste à crée une application de scraping pour analysé le site http://books.toscrape.com/.

---

### Environnement virtuel
Pour travailler sur ce projet, il est recommandé de configurer un environnement virtuel. Cela permettra de maintenir les dépendances du projet séparées des autres projets Python et d'éviter les conflits entre les différentes bibliothèques.

---

### Installation de l'environnement virtuel
Assurez-vous d'avoir Python 3 installé sur votre système. Sinon, vous pouvez le télécharger et l'installer à partir du site officiel de Python.

Ouvrez votre terminal (ou invite de commande) et accédez au répertoire de votre projet.

Pour créer un nouvel environnement virtuel, utilisez la commande suivante : python -m venv projet2_scraping

Cela créera un dossier appelé "projet2_scraping" qui contiendra l'environnement virtuel.

Activez l'environnement virtuel en utilisant la commande appropriée selon votre système d'exploitation :

Sur Windows : .\projet2_scraping\Scripts\activate
Sur macOS et Linux : source projet2_scraping/bin/activate

Vous saurez que l'environnement virtuel est actif lorsque vous verrez (projet2_scraping) devant votre invite de commande.
Maintenant que l'environnement virtuel est activé, vous pouvez installer les bibliothèques requises en utilisant la commande suivante : pip install requests bs4 os-csv

---

### Exécution du code
Avant d'exécuter le code, assurez-vous d'avoir activé l'environnement virtuel comme expliqué ci-dessus.
Pour exécuter le code, vous pouvez simplement exécuter le fichier Python à l'aide de la commande suivante : py projet2_scraping.py

---

# Code Python pour le scraping (projet2_scraping.py)

```
python
import os
import requests
import csv
from bs4 import BeautifulSoup

# Le code Python va ici ...

print("Extraction terminée avec succès !")

```

