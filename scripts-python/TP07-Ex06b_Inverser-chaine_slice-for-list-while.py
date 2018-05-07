# -*- coding: utf-8 -*-

#TP7-Ex2-5.9 Inverser une chaine de caractères

# En informatique, il est possible de résoudre un problème de plusieurs manières.
# Ici sont présentées plusieurs solutions pour inverser une chaine de caractères (et il y en a bien d'autres...)
# Vous devriez être capable de trouver une solution par vous-mêmes,
# de comprendre les différentes solutions/versions proposées ici,
# et d'appliquer une de ces solutions, en particulier si elle vous est demandée spécifiquement.

###############################################################################
###### Version 1 : while
print "\n -> Version 1 : "

# On va faire une boucle qui va parcourir tous les indices de la chaine, en allant du dernier au premier.
# En utilisant les indices, on mettra les caractères dans une nouvelle chaine un par un (à chaque itération de la boucle).
# Etant donné que l'on va du dernier caractère au premier caractère, cela mettra bien la chaine à l'envers.

# Pour connaitre la longueur de la chaine, on utilise la fonction len().
# Le numéro de la position du dernier caractère correspond à la longueur de la chaine moins 1.
# Exemple: Le positions des caractères vont de 0 à 4 pour une chaine de longueur 5.

chaine = "Salut"
# On initialise la variable chaineInverse à vide. Obligatoire pour pouvoir y ajouter des caractères plus tard.
chaineInverse = ""
# On fait une boucle avec i qui commencera à l'indice du dernier caractère de la chaine (len(chaine)-1)
# et diminuera de 1 à chaque itération (i = i-1 dans la boucle), jusqu'à l'indice du premier caractère (0)
i = len(chaine)-1
while i >= 0:
    # Pour construire la chaine inversée, à chaque passage dans la boucle, on ajoute le caractère corresponsant à l'indice. Soit du dernier au premier.
    chaineInverse += chaine[i] # équivaut à : chaineInverse = chaineInverse + chaine[i]
    i = i-1
print chaineInverse

###############################################################################
###### Version 2 : for
print "\n -> Version 2 : "

###### A SAVOIR
# for i in range (x,y,z)
# correspond à une boucle où i ira de x à y (non inclus).
# Rappel: avec un for, il n'est pas nécessaire d'initialiser la variable i avant le for
# et c'est le for qui se chargera de faire évoluer la valeur de i.
# (Contrairement à un while: si on utilise un compteur, il faut l'initialiser et le faire évoluer dans la boucle.)
# la variable z (optionnelle) indique la façon dont va évaluer i!
# Si on ne la met pas, cela correspond par défaut à z = 1, soit i augmente de 1 à chaque passage dans la boucle.

###Exemple1:
# for i in range (0,4,1) # équivaut à: for i in range (0,4) # équivaut à: for i in range (4)
# la variable i ira de 0 à 4 non compris en augmentant de 1 à chaque passage dans la boucle.
# i vaudra donc: 0, puis 1, puis 2, puis 3
for i in range (0,4,1):
    print i,
print

###Exemple2:
# for i in range (0,7,2)
# la variable i ira de 0 à 7 non compris en augmentant de 2 à chaque passage dans la boucle.
# i vaudra donc: 0, puis 2, puis 4, puis 6
for i in range (0,7,2):
    print i,
print

###Exemple3:
# for i in range (5,0,-1)
# la variable i ira de 5 à 0 non compris en diminuant de 2 à chaque passage dans la boucle.
# i vaudra donc: 5, puis 4, puis 3, puis 2, puis 1 
for i in range (5,0,-1):
    print i,
print

###### SOLUTION

chaine = "Salut"
chaineInverse = ""
# on fait une boucle avec i qui ira de l'indice du dernier caractère (1ere variable du range : len(chaine)-1 inclus)
# jusqu'à l'indice du premier caractère (2ème variable du range: -1 non inclus)
# en diminuant i de 1 à chaque passage dans la boucle (troisième variable du range: -1).
for i in range (len(chaine)-1,-1,-1):
    chaineInverse += chaine[i]
print chaineInverse

###############################################################################
###### Version 3 : version simple
print "\n -> Version 3 : "

# Plutôt que de parcourir la chaine du dernier au premier caractère pour les ajouter en fin de chaine.
# ex: chaineInverse = chaineInverse + chaine[i]
# On peut parcourir la chaine dans l'ordre normal et ajouter les caractères en début de chaine.
# ex: chaineInverse = chaine[i] + chaineInverse
# Cela inverse également la chaine de caractères!

# pour le for, on va utiliser ici:
# for i in chaine
# Rappel: cela permet de faire une boucle où i prendra pour chaque itération un caractère de la chaine,
# en les parcourant dans l'ordre. i vaudra donc directement un caractère (str), et non plus l'indice/la position (int).
# Exemple si la chaine vaut "Salut" :
# 1ere itération : i vaudra "S"
# 2eme itération : i caudra "a"
# etc...
# 5eme iteration : i vaura "t"

chaine = "Salut"
chaineInverse = ""
# on fait une boucle où i vaudra chaque caractère de chaine lors des itérations, dans l'ordre
for i in chaine:
    # On ajoute à chaque fois le caractère de l'itération (directement i ! ) en début de chaineInverse, ce qui inverse bien chaine.
    chaineInverse = i + chaineInverse
print chaineInverse

# A SAVOIR
# on a décidé d'utiliser une variable i pour le for, mais on peut tout à fait utiliser une autre variable.
# car, caractere, c, j, toto, etc...
# Exemple
chaine = "Salut"
chaineInverse = ""
for car in chaine:
    chaineInverse = car + chaineInverse
print chaineInverse

###############################################################################
###### Version 4 : slice
print "\n -> Version 4 : "

###### A SAVOIR
chaine = "Salut"
print "------------debut slice"
# print chaine[1] # caractère en position 1 de chaine: "a"
print chaine[1:4] #caractères de la position 1 à 4 non inclus: "alu"
print chaine[-1] #le dernier caractère: "t"
print chaine[-3] # 3eme caractère en partant de la fin: "l"
print chaine[0:-1] #caractères de la position 0 au dernier caractère non inclus: "Salu"
print chaine[:-1] #caractères du début au dernier caractère non inclus: "Salu"
print chaine[2:] #caractères de la position 2 à la fin: "lut"
# print chaine[3:1] #caractères de la position 3 à 1 non compris, en sens normal: "", pas possible, aucun caractere
# print chaine[3:1:1] #caractères de la position 3 à 1 non compris, en sens normal: "", pas possible, aucun caractere
print chaine[3:1:-1] #caractères de la position 3 à 1 non compris, en sens inverse: "ul"
print chaine[::-1] #caractères du début à la fin, en sens inverse: "tulaS"
print chaine[::2] #caractères du début à la fin, un caractère sur 2: "Slt"
print chaine[::-2] #caractères du début à la fin, un caractère sur 2 en sens inverse: "tlS"
#print chaine[1:4:-1] #caractères de position 1 à 4 non compris, en sens inverse: "", pas possible, aucun caractere
print chaine[4:1:-1] #caractères de position 4 à 1 non compris, en sens inverse: "tul"
print "------------fin slice\n"

###### SOLUTION
chaine = "Salut"
# affiche chaine à l'envers
print chaine[::-1]

###### A SAVOIR
# Note: chaine n'a pas été modifiée! print chaine[::-1] a simplement affiché la chaine à l'envers.
# Si on affiche chaine à nouveau, on constate qu'elle n'a pas changée:
print chaine
# Il est impossible de modifier une chaine de caractères.
# Pour changer une chaine de caractère qui se trouve dans une variable,
# il est obligatoire de faire une nouvelle assignation à cette variable.
chaine = chaine[::-1]
# La valeur de chaine a maintenant été remplacée par la chaine de caractères à l'envers::
print chaine

###############################################################################
###### Version 5 : liste
print "\n -> Version 5 : "

# Pour travailler les listes, on peut mettre tous les caractères dans une liste, puis utiliser la fonction reverse().
# Note: les affichages de la liste sont là uniquement pour voir l'évolution.

chaine = "Salut"
chaineInverse = ""
# La fonction list() permet de transformer directement une chaine de caractères en liste
listeCaracteres = list(chaine)
print listeCaracteres
# La fonction reverse() inverse entièrement les éléments de la liste.
# On note au passage que la liste a été modifiée! Une liste peut être modifiée même sans une nouvelle assignation.
listeCaracteres.reverse()
print listeCaracteres
# Une façon de parcourir les éléments d'une liste dans l'ordre est:  for i in list
# Ici les éléments sont les caractères de chaine qui ont été inversés, il suffit donc de les ajouter à chaineInverse
for i in listeCaracteres:
    chaineInverse += i
print chaineInverse

###############################################################################
###### Version 5 : liste et fonction
print "\n -> Version 6 : "

# On va utiliser la fonction join() pour afficher "proprement" une liste.
# la fonction ch.join(li) va renvoyer une chaine de caractères en intercalant 
# la chaine ch entre tous les éléments de la liste li (ou chaine) fournie en paramètre.

# Bref, ici après avoir transformé la chaine initiale en liste, l'avoir inversée avec reverse(),
# on va afficher les éléments en intercalant entre eux une chaine vide grâce à join().

chaine = "Salut"
listeCaracteres = list(chaine)
listeCaracteres.reverse()
chaineInverse = "".join(listeCaracteres)
print chaineInverse

###############################################################################
