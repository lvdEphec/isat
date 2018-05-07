# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 09:28:49 2018

@author: l.vandormael
"""
# code montré en TP
# TP 07 - Exercice 3 - compter le nombre de chiffres pairs, impairs et de zéros


# version 1 : en travaillant avec des entiers
print
print 'Version 1'

compteurPairs, compteurImpairs, compteurZeros = 0, 0, 0

nombreInitial = 1640
nombreRestant = nombreInitial

if nombreRestant == 0:
    compteurZeros += 1
else:
    while nombreRestant > 0:
            
        nombre = nombreRestant % 10
        
        if nombre == 0:
            compteurZeros += 1
        elif nombre % 2 == 0:
            compteurPairs += 1
        else :
            compteurImpairs +=1
        
        nombreRestant = nombreRestant // 10
    
print 'nombres pairs : %i, nombres impairs : %i, nombres zeros : %i ' \
       % (compteurPairs, compteurImpairs, compteurZeros)
       
       
       

# version 2 : en parcourant une chaine de caractères
print
print 'Version 2'

compteurPairs, compteurImpairs, compteurZeros = 0, 0, 0 

nombreInitial = 1640
nombreChaine = str(nombreInitial)

i = 0
while (i < len(nombreChaine)):
    
    nombre = int(nombreChaine[i])
        
    if nombre == 0:
        compteurZeros += 1
    elif nombre % 2 == 0:
        compteurPairs += 1
    else :
        compteurImpairs +=1
        
    i += 1
        

print 'nombres pairs : %i, nombres impairs : %i, nombres zeros : %i ' \
       % (compteurPairs, compteurImpairs, compteurZeros)
       
