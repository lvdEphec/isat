# -*- coding: utf-8 -*-

####################################TP7-Ex5
# pierre papier ciseaux
# avec break
# avec random

# Programme qui demande en boucle "Pierre, Papier, Ciseaux?" à l'utilisateur, qui fait un choix au hasard et qui compte les points.
# Possibilité de quitter le jeu et ainsi de voir s'afficher le résultat.

# Note : La structure générale du programme sera une boucle qui, à chaque fois, recevra le choix du joueur, le testera,
# fera un choix aléatoire si nécessaire, testera le gagnant, comptera les points puis affichera le score final après la sortie de la boucle.

# Importation de random pour pouvoir untiliser randint()
import random
# On initialise les points à 0
pointsJoueur, pointsOrdi, pointsEgalite = 0, 0, 0
# On définit ci-dessous des constantes, pour utiliser les entiers 1, 2 et 3
# en voyant directement à quelles valeurs ils correspondent.
# (Plus tard on pourra utiliser un "dictionnaire" à la place par exemple.)
PIERRE = 1
PAPIER= 2
CISEAUX = 3
# On fait ici une bloucle infinie! La seule façon de sortir sera donc d'utiliser un break
while True:
    choixJoueur = str(raw_input('"Pierre", "Papier", "Ciseaux"? ou "Fin"? : '))
    # S'il introduit "Fin", on quitte lesesa boucle en utilisant un break
    if choixJoueur == "Fin":
        break
    # S'il a introduit un bon choix pour jouer, alors...
    elif choixJoueur=="Pierre" or choixJoueur=="Papier" or choixJoueur=="Ciseaux":
        # Affichage du choix du joueur
        print "Tu choisis %s" % (choixJoueur)
        # Le programme fait un choix lui aussi, totalement aléatoire ici, grâce à la fonction randint().
        # Il lui suffit de choisir un entier de 1 à 3. On considère que chaque entier correspond à une valeur.
        # PIERRE == 1, PAPIER == 2, CISEAUX == 3
        choixOrdi = random.randint(1,3)
        # Le programme affiche ce qu'il a choisi de manière compréhensible à l'utilisateur.
        if choixOrdi == PIERRE:
            print "Je choisis Pierre"
        elif choixOrdi == PAPIER:
            print "Je choisis Papier"
        else:
            print "Je choisis Ciseaux"
        # On teste qui a gagné, perdu ou si c'est égalité, et on incrémente le bon score si nécessaire.
        # Rappel : le \ à la fin d'une ligne de code en python permet de continuer d'écrire cette ligne de code sur la ligne suivante.
        if (choixJoueur == "Pierre" and choixOrdi == CISEAUX) or \
            (choixJoueur == "Papier" and choixOrdi == PIERRE) or \
            (choixJoueur == "Ciseaux" and choixOrdi == PAPIER):
                pointsJoueur +=1
                print "Tu as gagné!"
        elif (choixJoueur == "Pierre" and choixOrdi == PAPIER) or \
            (choixJoueur == "Papier" and choixOrdi == CISEAUX) or \
            (choixJoueur == "Ciseaux" and choixOrdi == PIERRE):
                pointsOrdi +=1
                print "J'ai gagné!"
        else:
            pointsEgalite += 1
            print "Egalité!"
    # Si l'utilisateur a introduit quelque chose de non valide, on ne fait qu'afficher un message d'erreur dans cette itération de la boucle.
    else:
        print 'Veuillez introduire "Pierre", "Papier", "Ciseaux" ou "Fin".'
# Après la boucle, on affiche un récapitulatif des scores.
print "\nTon score : %i. Mon Score : %i. Egalite(s) : %i" % (pointsJoueur,pointsOrdi,pointsEgalite)
# Note: Vous souvenez-vous bien comment utiliser %i, %s, etc... pour afficher des combinaisons de textes et des variables?


# Note sur l'importation de librairies et de fonctions:
"""
# Ecrire par exemple:
import random
# importe toute la librairie random, et permet ensuite d'utiliser les fonctions de cette librairie comme ceci par exemple:
a = random.random()
b = random.randint(1,10)
# Alors qu'écrire ceci par exemple:
from random import randint
# importe une seule fonction à la fois d'une librairie (ici randint()), mais qui peut alors être utilisée directement, par exemple:
b = randint(1,10)
"""

# Note sur l'intelligence artificielle:
"""
# Si vous retenez ce que l'utilisateur a introduit lors des coups précédents,
# et que vous choisissez ce que le programme va jouer en fonction de ces coups précédents,
# vous développeriez alors une intelligence artificielle!
# Cependant... est-ce si simple que ça de battre ce programme qui est pourtant totalement aléatoire?
"""

# programme sans commentaires
"""
import random
pointsJoueur, pointsOrdi, pointsEgalite = 0 , 0, 0
PIERRE = 1
PAPIER= 2
CISEAUX = 3
while True:
    choixJoueur = str(raw_input('"Pierre", "Papier", "Ciseaux"? ou "Fin"? : '))
    if choixJoueur == "Fin":
        break
    elif choixJoueur=="Pierre" or choixJoueur=="Papier" or choixJoueur=="Ciseaux":
        print "Tu choisis %s" % (choixJoueur)
        choixOrdi = random.randint(1,3)
        if choixOrdi == PIERRE:
            print "Je choisis Pierre"
        elif choixOrdi == PAPIER:
            print "Je choisis Papier"
        else:
            print "Je choisis Ciseaux"
        if (choixJoueur == "Pierre" and choixOrdi == CISEAUX) or \
            (choixJoueur == "Papier" and choixOrdi == PIERRE) or \
            (choixJoueur == "Ciseaux" and choixOrdi == PAPIER):
                pointsJoueur +=1
                print "Tu as gagné!"
        elif (choixJoueur == "Pierre" and choixOrdi == PAPIER) or \
            (choixJoueur == "Papier" and choixOrdi == CISEAUX) or \
            (choixJoueur == "Ciseaux" and choixOrdi == PIERRE):
                pointsOrdi +=1
                print "J'ai gagné!"
        else:
            pointsEgalite += 1
            print "Egalité!"
    else:
        print 'Veuillez introduire "Pierre", "Papier", "Ciseaux" ou "Fin".'
print "\nTon score : %i. Mon Score : %i. Egalite(s) : %i" % (pointsJoueur,pointsOrdi,pointsEgalite)

"""
