# -*- coding: utf-8 -*-

#TP7-Ex5-10.9 Renvoyer "vrai" si l'argument transmis est un chiffre.

###############################################################################

##### A SAVOIR
print "\n -> A SAVOIR"
# Il existe de nombreuses fonctions utiles qui peuvent être appliquées sur une chaine.
# Les fonctions doivent toujours être avec des parenthèse à la fin de leur nom.
# Les arguments utilisés par la fonction se trouvent dans les parenthèses.
# Certaines fonctions n'ont pas besoin d'arguments, mais il faut tout de même mettre les parenthèses.
# Une fonction identique peut parfois fonctionner sans, avec un, ou avec plusieurs arguments, et réagir alors différemment.

# Note 1 : le traitement des caractères accentués n'est pas abordé dans le cadre de ce cours.

# Note 2 : Même si une fonction appliquée à une chaine de caractères peut renvoyer un résultat qui correspond
# à la chaine modifiée, la chaine initiale ne sera jamais directement modifiée par une fonction.
# Ex:

exemple = "Test"
print exemple.upper() # Affiche la chaine de caractères exemple en majuscule : TEST
print exemple # affiche la chaine de caractères exemple. On voit qu'elle n'a pas été modifiée : test
print

# Quelques fonctions: (Lancer le script pour voir les résultats s'afficher.)
chaine = "Bonjour , comment allez-vous? ...  "
print chaine.count("o") # compte le nombre de fois où la chaine de caractères indiquée se trouve dans chaine : 4
print chaine.count("ou") # 2
print
print chaine.find("ur") # renvoie la position de la chaine de caractère à retrouver dans chaine : 5
print chaine.find("o") # renvoie la première position s'il est trouvé plusieurs fois : 1
print chaine.find("y") # renvoie -1 s'il est trouvé plusieurs fois : -1
print
print chaine.isdigit() # renvoie True si chaine est composé uniquement de chiffres : False
print chaine.isalpha() # renvoie True si chaine est composé uniquement de lettres : False
print chaine.isalpha() # renvoie True si chaine est composé uniquement de chiffres ou de lettres : False
print chaine.islower() # renvoie True si chaine est composé uniquement de chiffres ou de lettres : False
print chaine.isupper() # renvoie True si chaine est composé uniquement de chiffres ou de lettres : False
print
print chaine.lower() # met chaine en minusculte : "bonjour , comment allez-vous? ... "
print chaine.upper() # met chaine en majuscule : "BONJOUR , COMMENT ALLEZ-VOUS? ... "
print chaine.lower().islower() # met chaine en minuscule, puisrenvoie True si la chaine est en minuscule: True
print
print chaine.replace(".","?") # remplace les "." par des "?" : "Bonjour , comment allez-vous? ???"
print chaine.replace("Bonjour","Salut") # remplace "Bonjour" par "Salut" : "Salut , comment allez-vous? ...  "
print
print chaine + "FIN" # "Bonjour , comment allez-vous? ...  FIN"
print chaine.strip() + "FIN" # enlève les blancs au début et à la fin : "Bonjour , comment allez-vous? ...FIN"
# enlève les blancs au début et à la fin, met en majuscule puis remplace "BONJOUR" par "salut"
print chaine.strip().upper().replace("BONJOUR","salut") + "FIN" # "salut , COMMENT ALLEZ-VOUS? ...FIN"
print
print len(chaine) # la longueur de la chaine : 35
print
chaine2 = "gaston"
print "*".join(chaine2) # la fonction join place "*" entre tous les caractères de chaine : g*a*s*t*o*n
print "ZZZ".join(chaine2) # gZZZaZZZsZZZtZZZoZZZn
chaine3 = "ZZZ"
print chaine3.join(chaine2) # gZZZaZZZsZZZtZZZoZZZn
print chaine3.join("gaston") # gZZZaZZZsZZZtZZZoZZZn
print
print chaine.split() # met tous les mots séparés par des blancs et les met dans une liste : ['Bonjour', ',', 'comment', 'allez-vous?', '...']



###############################################################################
##### SOLUTION

##### VERSION 1
print "\n -> Version 1"

argument = "fff5"
print argument.isdigit()

argument = "6587"
print argument.isdigit()

###############################################################################

##### VERSION 2
print "\n -> Version 2"

#### A SAVOIR
# x in chaine
# renvoie vrai si la chaine x est dans la chaine chaine
# Exemple:
print "a" in "tada" # affiche True
print "b" in "tada" # affiche false
print "ada" in "tada" # affiche True
print

############
x = "o" 
chaine = "ok"
print x in chaine # affiche True
print

############
if x in chaine: # le test est vrai
    print x + " est dans " + chaine # donc ce print est effectué
print

############
chiffres = "0123456789" # La chaine de caractères chiffres contient tous les chiffres
argument = "6"
if argument in chiffres: # Si argument se trouve dans la chaine de caractères chiffres
    print True #alors oon affiche True
print

#### SOLUTION
print "-> solution 2"
chiffres = "0123456789"
argument = "fff5"
resultat = True
for c in argument:
    if not(c in chiffres):
        resultat = False
        break
print resultat
        
chiffres = "0123456789"
argument = "6587"
resultat = True
for c in argument:
    if not(c in chiffres):
        resultat = False
        break
print resultat

