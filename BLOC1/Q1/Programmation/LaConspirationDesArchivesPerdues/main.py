import os
import sys

# La conspiration des Archives Perdues
'''
Réalisé par: Mathias Carsault
Le but de cet examen est de montrer que tu connais les bases de python et que tu sais les appliquer.
Comment gagner des points ? En leur montrant ce que tu sais faire: Ouverture de fichier, boucle, condition, fonction, dictionnaire,...
Idéalement, il faudrait d'abord faire les examens blancs "batman" et "Doctor Who" avant de faire celui-ci, ils sont plus faciles et la correction est sur mon github.

Me contacter: 
Mail: mathias.carsault@std.heh.be
Github: https://github.com/caimath
'''

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
                print(f"Dossier trouvé : {chemin_complet}")

                # Explorer récursivement le sous-dossier
                explorer_dossier(chemin_complet)


            # Vérifier si l'élément est un fichier
            elif os.path.isfile(chemin_complet):

                # Vérifier si l'élément est un fichier texte (Demandé dans la consigne) 
                if chemin_complet.endswith('.txt') and "buggy_file.txt" not in chemin_complet: # Exclure buggy_file.txt (Obstacle de taille)
                    print(f"Fichier texte trouvé : {chemin_complet}")

                    # Lire et afficher le contenu du fichier texte
                    try:
                        with open(chemin_complet, 'r', encoding="utf-8") as fichier:                                
                            contenu = fichier.readlines()

                            # Une cible à identifier (Trouver la ligne contenant "Ce qui")
                            for ligne in contenu:
                                if "Ce qui".lower() in ligne.strip().lower():
                                    print(f"Ce qui a été trouvé dans la ligne {ligne} dans le fichier {chemin_complet}")

                    except UnicodeDecodeError: # Gestion de l'erreur de décodage
                        print(f"Erreur de décodage du fichier : {chemin_complet}")





if __name__ == "__main__":

    # Chemin de base du dossier à explorer
    chemin_depart = 'archives_mission/'
    explorer_dossier(chemin_depart)

# Fin du programme