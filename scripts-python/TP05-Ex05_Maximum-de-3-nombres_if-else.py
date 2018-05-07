# -*- coding: utf-8 -*-

# TP06a-Ex05

# Programme qui recoit 3 nombres entiers et qui affiche le plus grand.
# Un avertissement est affiché si des nombres introduits sont identiques.
# Note: Le programme va plus loin que ce qui est demandé dans l'énoncé, en affichant combien de nombres sont identiques.

# VARIABLES ET CONSTANTES
messageDemande = "Entrez un nombre entier positif : "
messageReponse = "Le maximum est : "
messageEgalite = "Il y a %i nombres égaux."
maximum = None
nbEgalite = 0 # par défaut on considère que les nombres introduits ne sont pas égaux.

# RECEVOIR INPUT
# On convertit directement ce qui est introduit en entier.
# Si autre chose que des entiers est introduit -> ça plante.
a = int(input(messageDemande))
b = int(input(messageDemande))
c = int(input(messageDemande))

# TRAITEMENTS
# On va ensuite comparer les nombres introduits pour déterminer quel est le maximum. Une façon de faire:
if (a >= b) and (a >= c):
    maximum = a
elif (b >= a) and (b >= c):
    maximum = b
else:
    maximum = c

# NOTE: La fonction python "max" indiquée ci-dessous pourrait être utilisée à la place!
# maximum = max(a, b, b)

# On regarde s'il y a 3 nombres identiques introduits,
# sinon on regarde s'il y en a 2.
# On retient le nombre d'égalité en conséquence, grâce à la variable nbEgalite.
if (a == b == c):
    nbEgalite = 3
elif (a==b or a==c or b==c):
    nbEgalite = 2

# AFFICHER OUTPUT
print messageReponse + str(maximum) # ne pas oublier de convertir int -> str pour concaténer des str avec +
if nbEgalite:
  print messageEgalite % (nbEgalite) #Affiché seulement s'il y a des égalités


# TP4-Ex4-version2
"""
# Voici une autre version du programme, en utilisant une boucle "for" et un type "list".
# Note: ici l'avertissement indique s'il y a des nombres introduits identiques, mais pas leur nombre.

avertissement = ""
reponses = []
for i in range (3):
    reponse = int(input("Introduisez l'entier numero " + str(i+1) + " : "))
    if (reponse in reponses):
        avertissement = "Vous avez introduit au moins 2 nombres identiques!"
    reponses.append(reponse)

print "Le maximum est " + str(max(reponses)) + ". " + avertissement
"""
