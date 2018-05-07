# -*- coding: utf-8 -*-

# TP08-Ex07
# détection de nombre premier
# Le programme reçoit des nombres au clavier et affiche à chaque fois si c'est un nombre premier ou non.
# Lorsque l'utilisateur introduit "rien du tout", le programme s'arrête.

# Note: La structure générale du programme sera
# une première boucle qui recevra et traitera à chaque fois ce qui est introduit au clavier ainsi que
# une seconde boucle imbriquée dans cette première boucle et qui sera utilisée lorsqu'on désire tester si un nombre introduit est premier.
    
continuer = True
# On va faire une boucle tant que la variable "continuer" est à True (vrai) pour recevoir des nombres au clavier et les tester.
# Pour sortir de la boucle, il faudra donc soit mettre cette variable à False (faux), soit utiliser un "break".
while continuer :
    # On recoit quelque chose au clavier. On utilise raw_input sans déterminer le type, par défaut ce sera donc str.
    nombreIntroduit = raw_input("Introduisez un nombre. (N'introduisez rien pour quitter.) : ")
    # S'il a introduit rien du tout (soit, si on a reçu une chaine de caractères vide ""),
    # alors on affiche un message, puis on arrête la boucle pour quitter le programme.
    if (nombreIntroduit == ""):
        print "Au revoir!"
        continuer = False # alternative : break
    # Optionnel: sinon, on regarde s'il y a uniquement des chiffres qui ont été introduits grâce à la fonction isdigit().
    # la fonction isdigit() appliquée sur une chaine de caractères renvoie True s'il n'y a que des chiffre, et False sinon.
    # Si l'utilisateur a introduit autre chose que des chiffres (y compris les caractères "-" ou ".")
    # alors on ne fait qu'afficher un message d'erreur dans ce passage de la boucle.
    elif not( nombreIntroduit.isdigit() ):
        print "Veuillez introduire un nombre entier strictement positif."
    # sinon dans tous les autres cas (soit, on lorsqu'on n'a pas une chaine vide, et qu'elle contient uniquement des chiffres)
    else:
        # On transforme la chaine de caractères introduite en entier (toujours possible à ce stade vu qu'il n'y a que des chiffres)
        nombreIntroduit = int(nombreIntroduit)
        # Si cet entier est <= 0, on ne fait qu'afficher un message d'erreur dans ce passage de la boucle.
        # Note : on sait déjà ici que ça ne peut pas être <0 grâce au test avec isdigit()
        if nombreIntroduit <= 0:
            print "Erreur! Veuillez introduire un nombre entier strictement positif."
        #Sinon... (à ce stade on sait qu'on a un entier plus grand que 0 dans nombreIntroduit, on va enfin regarder s'il est premier)
        else :
            # On va regarder quels nombres divisent nombreIntroduit.
            # On sait que 1 et le nombre lui-même le divisent, on les exclut donc.
            # On va donc regarder si parmi les nombres de 2 à nombre-1, il y a des diviseurs.
            # Dès qu'un de ces nombres est diviseur (pas de reste après la division), alors on sait que le nombre n'est pas premier.
            # Concrètement...
            # On va commencer par tester 2 comme diviseur.
            diviseur = 2
            # Tant qu'on n'a pas trouvé de diviseur, on va considérer que le nombre est premier avec la variable nombrePremier
            nombrePremier = True
            # On va parcourir tout les nombre de 2 à nombre-1 grâce à une boucle
            # tant que diviseur est <= nombre -1
            # ET tant que nombrePremier n'indique pas que le nombre n'est pas premier
            # (par souci de performance, car ça ne sert à rien de continuer à tester les autres diviseurs si on en a déjà trouvé un)
            # alternative : utiliser un break lorsqu'on trouve un diviseur
            while (diviseur <= nombreIntroduit-1) and nombrePremier :
                # Si le diviseur testé divise le nombre (reste == 0), alors on met False dans nombrePremier, ce qui arrêtera la boucle
                if (nombreIntroduit % diviseur) == 0:
                    nombrePremier = False
                # A chaque passage de la boucle on incrémente le diviseur pour tester le nombre suivant au prochain passage
                diviseur += 1 #pourrait être dans un else...
            # Après la boucle, si nombrePremier est toujours à True, alors on affiche "Premier" car on n'a trouvé aucun diviseur.
            # Sinon, on affiche "Pas premier". nombrePremier vaut False car on a trouvé au moins un diviseur parmi les nombres de 2 à nombre-1
            if nombrePremier:
                print "Nombre premier."
            else:
                print "Ce nombre n'est pas premier."


# Note: pour des raisons de performance, on commence par tester si les plus petits nombres sont diviseurs, 
# car ils ont plus de chance d'être diviseurs!
# A tester : Si on teste les diviseurs en allant de nombreIntroduit-1 à 2 et en introduisant
# un très grand nombre introduit, que se passe-t-il?
# Réponse: Le programme tourne longtemps car il fait beaucoup d'itérations dans la boucle avant de trouver un diviseur.
# Il fait donc la même chose, mais de manière bien moins performante!

#code sans commentaires
"""
continuer = True
while continuer :
    nombreIntroduit = raw_input("Introduisez un nombre. (N'introduisez rien pour quitter.) : ")
    if (nombreIntroduit == ""):
        print "Au revoir!"
        continuer = False
    elif not( nombreIntroduit.isdigit() ):
        print "Veuillez introduire un nombre entier strictement positif."
    else:
        nombreIntroduit = int(nombreIntroduit)
        if nombreIntroduit <= 0:
            print "Erreur! Veuillez introduire un nombre entier strictement positif."
        else :
            diviseur = 2
            nombrePremier = True
            while (diviseur <= nombreIntroduit-1) and nombrePremier :
                if (nombreIntroduit % diviseur) == 0:
                    nombrePremier = False
            if nombrePremier:
                print "Nombre premier."
            else:
                print "Ce nombre n'est pas premier."
"""
