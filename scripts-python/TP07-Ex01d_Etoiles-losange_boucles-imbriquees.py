# -*- coding: utf-8 -*-


# 1) Version demandée
# 2) Version avec paramètre pour la hauteur
# 3) Versions courtes

##### 1) Version demandée ##################################

# On va commencer par dessiner un triangle sur 5 lignes, puis on fera un triangle renversé sur les 5 lignes suivantes.

# PREMIER TRIANGLE
# On sait que l'on veut afficher 5 lignes. Par exemple, de 1 à 5.
# On aura donc un premier while principal qui fera 5 itérations, en affichant à chaque fois quelque chose sur une ligne.
# On sait ensuite que sur chaque ligne, on veut afficher un certain nombre d'espaces puis un certains nombre d'étoiles.
# On aura donc deux whiles qui se suivent dans le grand While principal.
# Le premier while servira à ajouter le nombre d'espaces désiré à chaque ligne.
# Le second while servira à ajouter le nombre de blancs désiré à chaque ligne.
# 
### RESUME : On aura un while avec 5 itérations pour afficher 5 lignes.
# Dans ce while, on aura 2 whiles qui se suivent, pour ajouter les espaces puis les étoiles à afficher à chaque ligne.
#
### WHILE POUR LES ESPACES
# On sait que le nombre d'espaces à afficher à chaque ligne dépend du numéro de ligne.
# Ici, l'évolution du nombre d'espaces semble être régulière, la relation sera donc linéaire.
# Regardons le lien entre le numéro de ligne et le nombre d'espaces à afficher.
# Soit i le numéro de ligne et j le nombre d'espaces, on cherche la relation j = ? i + ?
# Le tableau ci-dessous est rempli simplement en comptant les lignes et les espaces sur le schéma de l'énoncé.
#
# ligne i : j espaces
#--------------------
# ligne 1 : 4 espaces
# ligne 2 : 3 espaces
# ligne 3 : 2 espaces
# ligne 4 : 1 espaces
# ligne 5 : 0 espaces
#
# On voit que lorsque i augmente de 1, j diminue de 1, on a donc -1 comme pente.
# Ensuite, on veut savoir combien vaut j lorsque i vaut 0.
# A l'inverse, on voit que lorsque i diminue de 1, j augmente de 1. On peut donc en déduire en partant de ligne 1 :
# ligne 0 : 5 espaces
# Ce qui nous donne la relation:
# j = -i + 5
# On sait donc maintenant déterminer le nombre d'espaces nécessaires en fonction du numéro de ligne.
# Vous pouvez tester. Par exemple, ligne 3 : -3+5 = 2, il nous faut bien 2 espaces.
#
### WHILE POUR LES ETOILES
# Il faut maintenant trouver le nombre d'étoiles que l'on veut ajouter en fonction de la ligne qu'on va afficher.
# Soit i le numéro de ligne et k le nombre d'espaces, on cherche la relation k = ? i + ?
# Comptons...
#
# ligne i : k étoiles
#--------------------
# ligne 1 : 1 étoiles
# ligne 2 : 3 étoiles
# ligne 3 : 5 étoiles
# ligne 4 : 7 étoiles
# ligne 5 : 9 étoiles
#
# On voit que lorsque i augmente de 1, k augmente de 2, on a donc 2 comme pente.
# A l'inverse, on voit que lorsque i diminue de 1, j diminue de 2. On peut donc en déduire:
# ligne 0 : -1 étoiles (ce ne serait pas possible d'afficher cela, mais ça nous aide à trouver la relation.)
# Ce qui nous donne la relation:
# k = 2i - 1
# On sait donc maintenant déterminer le nombre d'étoiles nécessaires en fonction du numéro de ligne.
# Vous pouvez tester. Par exemple, ligne 3 : 2*3-1 = 5, il nous faut bien 5 étoiles.
#
### RESUME
# On sait combien d'espaces et d'étoiles il faudra afficher en fonction du numéro de ligne (i).
# -1+5 espaces et 2i-1 étoiles
#
# ligne 1 ; i vaut 1 ; j vaut -1+5 = 4 espaces ; k vaut 2*1-1 = 1 étoile
# ligne 2 ; i vaut 2 ; j vaut -2+5 = 3 espaces ; k vaut 2*2-1 = 3 étoiles
# ligne 3 ; i vaut 3 ; j vaut -3+5 = 2 espaces ; k vaut 2*3-1 = 5 étoiles
# etc...

# SECOND TRIANGLE
# Pour afficher ensuite le triangle renversé, on fera un second while principal qui affichera 5 lignes,
# et on mettra dedans à nouveau 2 while qui se suivent pour afficher les espaces puis les étoiles.
# A nouveau, le nombre d'espaces et d'étoiles dépendra du numéro de ligne.
# En comptant dans l'énoncé... 
# ligne i : j espaces
# ligne 1 : 0 espaces
# ligne 2 : 1 espaces
# ...
# relation : j = i-1
# et
# ligne i : k espaces
# ligne 1 : 9 étoiles
# ligne 2 : 7 étoiles
#...
# relation : k = -2i+11


# LE CODE CONCRETEMENT
# La premiere boucle qui ira de 1 à 5, pour afficher au total 5 lignes.
# i correspondra donc au numéro de ligne
print "VERSION DEMANDEE"
i = 1
while i <= 5:
    # On vide la chaine ch, avant de lui ajouter les espaces puis les étoiles.
    ch=''
    # Ci-dessous le while qui affiche les espaces. Ce nombre dépend du numéro de ligne, soit i.
    # On a déterminé que le nb d'espaces vaut -i+5. On passe donc -i+5 fois dans la boucle en ajoutant 1 espace à chaque fois.
    j = 1
    while j <= 5-i:
        ch += " "
        j += 1
    # le while qui affiche les étoiles maintenant. Ce nombre dépend du numéro de ligne, soit i.
    # On a déterminé que le nb d'étoiles vaut 2i-1. On passe donc 2i-1 fois dans la boucle en ajoutant 1 étoile à chaque fois.
    k = 1
    while k <= 2*i-1:
        ch += "*"
        k += 1
    # Maintenant qu'on a contruit ch en ajoutant les espaces puis les étoiles, on l'affiche simplement...
    print ch
    # ... et on incrémente le i du while principal, pour passer à la ligne suivante.
    i+=1
# A ce stade, à la sortie de la boucle, le premier triangle est affiché.

# Affichage du triangle renversé maintenant, sur le même principe.
i = 1
while i <= 5:
    ch=''
    j = 1
    while j <= i-1:
        ch += " "
        j += 1
    k = 1
    while k <= 11-(2*i):
        ch += "*"
        k += 1
    print ch
    i+=1

    
##### 2) Version avec paramètre  pour la hauteur ##################################

# Pour pouvoir déterminer la taille du triangle en changeant une seule variable.

# Pour aller plus loin...
# Il faut remarquer que les relations sont directement dépendantes du nombre de lignes à afficher.
# Soit n le nombre de lignes sur lesquelles on affiche un triangle:
# premier triangle, la relation entre nb espaces et num ligne: j = -i + n
# premier triangle, la relation entre nb étoiles et num ligne: k = 2i - 1
# triangle renversé, la relation entre nb espaces et num ligne: j = i-1
# triangle renversé, la relation entre nb étoiles et num ligne: k = -2i+(2n+1)
   
# En ajoutant simplement la variable n, en l'utilisant pour le nombre d'itérations
# et en basant bien les relations entre le nb d'espaces et d'étoiles et le num de ligne sur cette variable,
# on peut maintenant influencer sur la taille des 2 triangles uniquement en modifiant cette variable n. 

print "\nVERSION AVEC PARAMETRE POUR LA HAUTEUR"
n = 8 # changement, choisir la taille ici
i = 1
while i <= n: # changement
    ch=''
    j = 1
    while j <= n-i:# changement
        ch += " "
        j += 1
    k = 1
    while k <= 2*i-1:
        ch += "*"
        k += 1
    print ch
    i+=1

i = 1
while i <= n: # changement
    ch=''
    j = 1
    while j <= i-1:
        ch += " "
        j += 1
    k = 1
    while k <= ((2*n)+1)-(2*i): # changement
        ch += "*"
        k += 1
    print ch
    i+=1


##### 3) Versions courtes ##################################

# Les boucles for s'écrivent habituellement de manière plus courte que les boucles while.
# Lorsqu'on sait à l'avance le nombre d'itération, elles sont généralement plus intéressantes.

# On remarque que les boucles intérieures ne servent qu'à obtenir le nombre désiré d'espaces et d'étoiles.
# Il est possible de multiplier une chaine de caractère par un nombre pour obtenir le même résultat.
# Pour construire la chaine à afficher, en multipliant une chaine " " et une chaine "*",
# on utilisera les mêmes valeurs dépendantes de i pour obtenir les nombres d'étoiles et d'espaces.

#version courte hauteur de 10
print "\nVERSION COURTE HAUTEUR 10"
for i in range(1,6):
    st = (-i+5) * " " + (2*i-1) * "*"
    print st
for i in range(1,6):
    st = (i-1) * " " + (-2*i+11) * "*"
    print st

#version courte avec paramètre
print "\nVERSION COURTE AVEC PARAMETRE POUR LA HAUTEUR"
n=3
for i in range(1,n+1):
    st = (-i+n) * " " + (2*i-1) * "*"
    print st
for i in range(1,n+1):
    st = (i-1) * " " + ((-2*i)+((2*n)+1)) * "*"
    print st
    
#version courte avec paramètre et une seule boucle... mais un else.
print "\nVERSION COURTE AVEC UNE SEULE BOUCLE ET AVEC PARAMETRE POUR LA HAUTEUR"
n=2
for i in range(1,(2*n)+1):
    if i <= n:
      st = (-i+n) * " " + (2*i-1) * "*"
      print st
    else:
      st = ((i-n)-1) * " " + ((-2*(i-n))+((2*n)+1)) * "*"
      print st

