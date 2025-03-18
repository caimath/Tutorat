import os
import sys

# La conspiration des Archives Perdues
'''
Réalisé par: Mathias Carsault
Le but de cet examen est de montrer que tu connais les bases de python et que tu sais les appliquer.
Comment gagner des points ? En leur montrant ce que tu sais faire: Ouverture de fichier, boucle, condition, fonction, dictionnaire,...
Idéalement, il faudrait faire les examens blancs "batman" et "Doctor Who" avant de faire celui-ci, ils sont plus faciles et la correction est sur github.

PS: Je n'ai trouvé aucun fichier où il est écrit "Ce qui" dedans donc si le programme ne renvoie rien avec ça c'est normal.

Me contacter: 
Mail: mathias.carsault@std.heh.be
Github: https://github.com/caimath
Github tutorat: https://github.com/caimath/Tutorat
'''

# Étape 1 et 2: Fonction pour explorer les dossiers et vérifier l'existence du premier dossier dans lequel on veut chercher
def explorer_dossier(chemin):

    '''
    1. Ici, dans le premier loop de la boucle, on prend en argument le chemin du dossier archives_mission
    2. Puis, si c'est un dossier, on affiche le message "Dossier trouvé : {chemin_complet}"
    3. Ensuite, on appelle la fonction explorer_dossier(chemin_complet) pour explorer récursivement le sous-dossier
    '''

    # Vérifier si le dossier existe (Toujours bon de vérifier et en +, c'est demandé dans la consigne)
    if os.path.exists("archives_mission") == True:

        # Parcourir tous les éléments dans le répertoire donné
        for element in os.listdir(chemin):
            chemin_complet = os.path.join(chemin, element) # Permet de créer le chemin complet de l'élément, en étant compatible avec tous les OS
            # Chemin = le chemin de base et si element est un dossier on obtient chemin/element --> permet d'explorer le dossier pour trouver les fichiers

            # Vérifier si l'élément est un dossier
            if os.path.isdir(chemin_complet):

                # Explorer récursivement le sous-dossier
                explorer_dossier(chemin_complet)


            # Vérifier si l'élément est un fichier
            elif os.path.isfile(chemin_complet):

                # Vérifier si l'élément est un fichier texte (Demandé dans la consigne) 
                if chemin_complet.endswith('.txt') and "buggy_file.txt" not in chemin_complet: # Exclure buggy_file.txt (Étape 4: Obstacle de taille)
                    print(f"Fichier texte trouvé : {chemin_complet}")

                    # Lire et afficher le contenu du fichier texte
                    try:
                        with open(chemin_complet, 'r', encoding="utf-8") as fichier:    
                            # Lire le contenu du fichier                            
                            contenu = fichier.read()

                            # Étape 5: Le Mur de la Cryptographie
                            # Passer le contenu du fichier dans la fonction de déchiffrement
                            texte_dechiffre = dechiffrer_cesar(contenu)
                            print(f"Contenu déchiffré du fichier {chemin_complet}:\n{texte_dechiffre}\n")

                            # Étape 4: Une cible à identifier (Trouver la ligne contenant "Ce qui")
                            if "Ce qui".lower() in texte_dechiffre.strip().lower():
                                print(f"'Ce qui' a été trouvé dans le fichier {chemin_complet}")
                            

                            # Étape 6: Un Rapport à Sécuriser
                            # Chiffrer le texte déchiffré
                            texte_chiffre = chiffrer_cesar(texte_dechiffre)
                            print(f"Contenu du fichier {chemin_complet}, correctement chiffré ")

                    except UnicodeDecodeError: # Gestion de l'erreur de décodage
                        print(f"Erreur de décodage du fichier : {chemin_complet}")
                        


# Étape 5: Le Mur de la Cryptographie
def dechiffrer_cesar(texte, decalage=3):
    # Créer une liste pour stocker le résultat du déchiffrement
    resultat = []

    for caractere in texte:

        # Vérifier si le caractère est une lettre
        if caractere.isalpha():
            # Déterminer si la lettre est majuscule ou minuscule
            base = 'A' if caractere.isupper() else 'a'

            # Calculer la nouvelle position de la lettre
            nouvelle_position = (ord(caractere) - ord(base) - decalage) % 26
            # ord() permet de convertir un caractère en son code ASCII

            # Convertir la nouvelle position en lettre
            nouvelle_lettre = chr(nouvelle_position + ord(base))
            resultat.append(nouvelle_lettre)

        else:
            # Si ce n'est pas une lettre, conserver le caractère tel quel
            resultat.append(caractere)

    return ''.join(resultat)


# Étape 6: Un Rapport à Sécuriser
# Même principe que la fonction de déchiffrement, mais avec un décalage positif
def chiffrer_cesar(texte, decalage=3):
    resultat = []
    for caractere in texte:
        if caractere.isalpha():
            base = 'A' if caractere.isupper() else 'a'
            nouvelle_position = (ord(caractere) - ord(base) + decalage) % 26
            # Ici on fait + au lieu de - pour chiffrer


            nouvelle_lettre = chr(nouvelle_position + ord(base))
            resultat.append(nouvelle_lettre)
        else:
            resultat.append(caractere)
    return ''.join(resultat)




# Initialisation du programme
if __name__ == "__main__":

    # Étapes 1 à 4
    # Chemin de base du dossier à explorer
    chemin_depart = 'archives_mission/'
    explorer_dossier(chemin_depart)

# Fin du programme