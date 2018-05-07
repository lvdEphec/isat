# -*- coding: utf-8 -*-

#TP7-Ex2-5.6

# Faire un programme qui regarde si un caractère est présent dans une chaine de caractères.
# (Dans les exemples on va regarder si le caractère 'u' est présent.
# Il est très facile de changer pour le caractère 'e', comme demandé dans l'énoncé.)

###############################################################################

# A SAVOIR
print "-> A savoir"
# On peut accéder directement à un caractère d'une chaine de caractère (string), grâce aux crochets []
# Exemple:

chaine = "salut"
print chaine[1]
# Affiche : a

# En effet, l'indice du premier caractère vaut 0. Les 5 caractères de cette chaine vont donc de 0 à 4.

# NOTE : si on fait une boucle avec i allant de 0 à 4, i représenterait l'indice de tous les caractères de la chaine.
# Cela est pratique car chaine[i] prend alors les valeurs de chaque des caractères, en les parcourant dans l'ordre.
# Exemple d'une boucle avec i allant de 0 à 4 (donc 5 itérations), avec chaine = "salut":
ch = "salut"
for i in [0, 1, 2, 3, 4]:
    print ch[i]
# itération 1 : i vaut 0 et donc ch[i] vaut ch[0] soit "s"
# itération 2 : i vaut 1 et donc ch[i] vaut ch[1] soit "a"
# itération 3 : i vaut 2 et donc ch[i] vaut ch[2] soit "l"
# itération 4 : i vaut 3 et donc ch[i] vaut ch[3] soit "u"
# itération 5 : i vaut 4 et donc ch[i] vaut ch[4] soit "t"

# Ensuite, il existe des fonctions utilisables directement sur les string (ou les list).
# Exemple, len() pour connaitre la longueur:

chaine = "salut"
print len(chaine)
# Affiche : 5

###############################################################################

# LE PROGRAMME VERSION 1 : boucle WHILE
# On va utiliser:
# - une variable < chaine > qui contient la chaine de caractère (on pourrait la recevoir au clavier), ici "salut"
# - une variable < caractere > qui contient le caractère recherché, ici "u" ("e" dans l'énoncé)
# - une variable i qui sera le compteur de notre boucle, initialisée à 0

# On va donc faire une boucle avec i allant de 0 jusqu'à la longueur de la chaine moins 1.
# Grâce au i, on testera aisément chaque caractère de la chaine dans l'ordre.
# si jamais le caractère cherché est trouvé, on affiche "caractère 'u' trouvé"
# et on fait un break pour sortir de la boucle.

print "\n-> Version 1"

chaine = "salut"
caractere = "u"
# La boucle avec i allant de 0 à 4 dans ce cas-ci
i = 0
while i < len(chaine)-1:
    # ch[i] prend à chaque itération une valeur d'un caractère de la chaine "salut", dans l'ordre.
    # si jamais un caractère de la chaine vaut le caractère recherché, alors on affiche et on fait un break.
    if chaine[i] == caractere:
        print "caractere '" + caractere + "' trouve à l\'indice : " + str(i)
        break
    i += 1

# NOTE1: Si on ne fait pas de break, la boucle continuera, et le texte "caractère 'u' trouvé" s'affichera simplement
# plusieurs fois si il est présent plusieurs fois. Ici, ça ne sert à rien de continuer si on a trouvé.

# NOTE 2: Si le caractère n'est pas trouvé, rien ne s'affichera.
# On pourrait utiliser une variable < trouve > (par exemple) # initialisée à False,
# et qu'on mettrait à True si le caractère est trouvé. On pourrait alors faire l'affichage après la
# boucle, en affichant "trouvé" ou "non trouvé" en fonction de la valeur de la variable < trouve >.


###############################################################################
    
# VERSION 2 : FOR
#
# Rappel:
#
# for i in range (fin)
# fait une boucle avec pour chaque itération i un entier qui ira de 0 à fin-1
#
# identique à 
# for i in range (0,fin)
    
print "\n-> Version 2"

chaine = "salut"
caractere = "u"
# une boucle avec i allant de  à longueur de chaine moins 1
for i in range (len(chaine)):
    if chaine[i] == caractere:
        print "caractere '" + caractere + "' trouve à la position : " + str(i)
        break

###############################################################################

# VERSION 3 : FOR en parcourant directement les caractères dans la boucle
#
# for c in chaine
# fait une boucle avec pour chaque itération c qui vaudra un caractère de chaine, dans l'ordre
# c sera donc dans ce cas-ci de type str et non int!
# Cette façon de faire fonctionne pour les chaines de caractères et également pour les listes
# NOTE : "c" n'est ici qu'un nom de varaiable. A la place ce pourrait très bien être car, i, x ou toto par exemple.

print "\n-> Version 3"

chaine = "salut"
caractere = "u"
for c in chaine:
    # on compare directement i, qui vaut ici un caracère de chaine
    if c == caractere:
        print "caractere '" + caractere + "' trouve!"
        break
 
###############################################################################   

# VERSION 4 : FOR en parcourant directement les caractères dans la boucle tout en ayant l'indice
#
# for i,j in enumerate(chaine)
# fait une boucle avec pour chaque itération dans ce cas-ci
# - i qui sera le compteur (int)
# - c qui sera le caractère (str)

print "\n-> Version 4"

chaine = "salut"
caractere = "u"
for i, c in enumerate(chaine):
    # on compare directement j, qui vaut ici un caracère de chaine
    if c == caractere:
        # on utilise le compteur i dans l'affichage
        print "caractere '" + caractere + "' trouve à la posisiton : " + str(i)
        break

###############################################################################

# VERSION 5 : en regardant directement si le caractère est dans la chaine
#
# Il est possible de tester directement si un caractère (ou une chaine de caractère)
# se trouve dans une autre chaine de caractères

print "\n-> Version 5"
chaine = "salut"
caractere = "u"
# on regarde simplement si < caractere > est dans < chaine >
if caractere in chaine:
    print "caractere '" + caractere + "' trouve!"

###############################################################################

# VERSION 6 : en utilisant une fonction définie pour les str pour tester si le caractère est présent
#
# Avec les chaines de caractères il est possible d'utiliser la fonction find().
# Elle renvoie la position. Si ce n'est pas trouvé, elle renvoie -1.

print "\n-> Version 6"
chaine = "salut"
caractere = "u"
# si find renvoie autre chose que -1, c'est que < caractere > est trouvé dans < chaine >
if chaine.find(caractere) != -1:
    # on peut utiliser la fonction find() pour afficher la position du caractère trouvé
    print "caractere '" + caractere + "' trouve a la position : " + str(chaine.find(caractere))
 
###############################################################################
