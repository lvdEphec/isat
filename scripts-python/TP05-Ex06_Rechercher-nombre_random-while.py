# -*- coding: utf-8 -*-

#TP06a-EX06

# CODE AVEC COMMENTAIRES

# Ce programme permet de déterminer un entier au hasard, puis de recevoir des nombres en input.
# En fonction du nombre aléatoire déterminé et du dernier nombre introduit par l'utilisateur,
# le programme affichera à chaque fois "plus grand", "plus petit" ou "trouvé" pour aider l'utilisateur à trouver le nombre tiré au hasard.
# Lorsque l'utilisateur trouve le bon nombre, le programme s'arrête.


# On importe la fonction "randint" de la librairaie "random".
from random import randint
# Nous pourrons donc dorénavant utiliser la fonction "randint" dans notre code.
# La fonction "randint" renvoie un entier déterminé aléatoirement.
# "random" est un mot anglais qui signifie "aléatoire" en français.
# Dans la ligne ci-dessous, on met donc dans la variable "nombreCherche" un entier aléatoire compris entre 0 et 100 inclus.
nombreCherche = randint(0,100)
# On initialise la variable "trouve" à False, pour indiquer que le nombre recherché n'a pas encore été trouvé.
trouve = False
# On aurait pu utiliser 0 à la place de False.

# Tant qu'on n'a pas trouvé, on recommence à exécuter le bloc de code du "while"
while not(trouve):
    # on recoit un nombre au hasard
    nombreIntroduit = int(input("Introduisez un nombre : " ))
    # on regarde s'il est plus grand, pour afficher "plus petit"
    if (nombreIntroduit > nombreCherche):
        affichage = "Le nombre recherche est plus petit"
    # on regarde s'il est plus petit, pour afficher "plus grand"
    elif (nombreIntroduit < nombreCherche):
        affichage = "Le nombre recherche est plus grand"
    # Sinon, s'il n'est ni plus grand, ni plus petit, c'est qu'il s'agit du nombre recherché.
    # Dans ce cas on affiche "trouvé"
    # et on met True (ou 1) dans la variable "trouve", pour indiquer que le nombre est trouvé et pouvoir sortir de la boucle "while".
    else :
        affichage = "Trouvé!"
        trouve = True
    # On affiche le résultat de ce passage dans le bloc de la boucle while (soit "plus grand", "plus petit" ou "trouvé")
    # Note: il est possible de faire directement des print sans passer par une variable "affichage".
    print affichage


# CODE SANS COMMENTAIRES
"""
from random import randint
nombreCherche = randint(0,100)
trouve = 0

while not(trouve):
    nombreIntroduit = int(input("Introduisez un nombre : " ))
    if (nombreIntroduit > nombreCherche):
        affichage = "Le nombre recherche est plus petit"
    elif (nombreIntroduit < nombreCherche):
        affichage = "Le nombre recherche est plus grand"
    else :
        affichage = "Trouvé!"
        trouve = 1
    print affichage
"""

# AUTRE VERSION SANS PASSER PAR UNE VARIABLE DE TYPE BOOLEEN
"""
from random import randint
nombreCherche = randint(0,100)
nombreIntroduit = None  #cette initialisation permet de rentrer dans la boucle, car None est < que les entiers

while (nombreIntroduit != nombreCherche):
    nombreIntroduit = int(input("Introduisez un nombre : " ))
    if (nombreIntroduit > nombreCherche):
        affichage = "Le nombre recherche est plus petit"
    elif (nombreIntroduit < nombreCherche):
        affichage = "Le nombre recherche est plus grand"
    else :
        affichage = "Trouvé!"
    print affichage
"""

# Pour info : utilisation de la fonction "random()":
"""
# La fonction "random" de la librairaie "random" renvoie un réel aléatoire entre 0 et 1
# La fonction "floor" de la librairie "math" renvoie un nombre arrondi à l'entier inférieur le plus proche. 

# Il faut importer ces fonctions pour pouvoir les utiliser.
from random import random
from math import floor
# Un réel (de type float) compris entre 0 (inclus) et 1 (non inclus).
a = random()
# En multipliant par 101, on obtient alors un réel (de type float) compris entre 0 (inclus) et 101 (non inclus).
a = 101*random()
# En arrondissant ensuite à l'entier inférieur, on obtient un nombre entier (mais toujours de type float!) compris entre 0 et 100
a = floor(101*random())
# En transformant un type float vers un type int en python, il n'y a pas d'arrondi. Seule la partie entière est conservée.
# Cela implique qu'en transformant un float vers un int on obtient le nombre un arrondi à l'entier inférieur.
# un nombre entier (de type int) compris entre 0 et 100.
a = int(101*random())
# Faire "randit(0,100)" revient donc au même que faire "int(101*random())".
"""

