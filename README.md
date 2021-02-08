[![Build Status](https://www.travis-ci.com/MaewenPell/P8_pur_beurre.svg?branch=main)](https://www.travis-ci.com/MaewenPell/P8_pur_beurre)
# Pur Beurre Project

## Introduction

Ce programme permet de substituer des aliments par d'autres meilleurs pour la santé et de pouvoir les sauvegader. Il se présente avec une interface User Friendly.

Il se base sur les données publique de la base de donnée [OpenFoodFact](https://fr.openfoodfacts.org/decouvrir).


Les aliments sont repertoriés et il vous sera possible d'effectuer une recherche pour les retrouver.

Sur la page d'accueil par exemple il vous suffit d'écrire "Nutella" pour trouver des substituts à cet aliment. Si vous vous créez un compte vous pourrez alors le sauvegarder dans vos favoris.

Les bienfais alimentaires des aliments sont basés sur leur nutriscrore. "A" étant la meilleure note et "E" la moins bonne.

----------------------- 

## Pré-requis

Ce programme est écrit en Python3 / Django et le systeme de base de donnée utilisé est PostgreSQL.
Vous aurez besoin pour lancer ce programme :

- [Python3](https://www.python.org/)

Pour installer les dépendances vous aurez également du gestionnire de package (PyPi)

- [Pip](https://pip.pypa.io/en/stable/installing/)

- [PostgreSQL](https://www.postgresql.org/download/)

Vous devrez installer les dépendences : 

```bash
pip install -r requirements.txt
```

## Installation

Vous devrez ajouter votre clé secrete dans le fichier settings.py.

Ensuite vous pourrez lancer les commande :
```bash
./manage.py migrate
```

Enfin pour remplir la base de donnée vous pourrez lancer la commande :
```bash
./manage.py populate
```

---------

## Lancement

1. Lancez le programme :
```bash
    ./manage.py runserver
```

2. Vous pouvez désormais vous rendre sur le site:
```
127.0.0.1
```


-------------------

## Paramètres

Plusieurs paramètres sont configurables et trouvables dans le fichier : "store/store_settings.py":


1. NB_RESULTS : 
    - Nous avons fait le choix de prendre 50 catégories parmis les plus fournies d'OpenFoodFact (les 50 premières par odre de remplissage), mais si vous le desirez vous pouvez changer ce nombre. Ensuite nous avons décider de les remplir avec 100 aliments.

