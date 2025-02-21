# Batman l'exam blanc

'''
Réalisé par: Mathias Carsault
Le but de cet examen est de montrer que tu connais les bases de python et que tu sais les appliquer.

Comment gagner des points ? En leur montrant ce que tu sais faire: Ouverture de fichier, boucle, condition, fonction, dictionnaire,...

- Quand tu ouvres un fichier, il faut bien le refermer après utilisation.
- Tu dois coder une fonction pour chaque paragraphe en général.
- Essayer de gérer les erreurs que l'utilisateur pourrait faire et essayer d'envisager tout les cas (utilisaion de try except et if elif else), si il rentre une mauvaise valeur, tu dois lui redemander de rentrer une valeur correcte.
- Le code ne doit surtout pas planter, d'où le but de gérer les erreurs et les entrées de l'utilisateur.
- Éviter les boucles infinies, sauf si c'est nécessaire. Dans ce cas ci, c'est nécessaire dans la fonction bat_signal (demandé dans l'énoncé).
- Commenter ton code pour expliquer ce que tu fais.
- Faire des tests unitaires (je les ajouterai bientot sur github)


Me contacter: 
Mail: mathias.carsault@std.heh.be
Github: https://github.com/caimath

'''

# Variable globale: dictionnaire de gadget, on va s'en servir pour ajouter, supprimer, modifier des gadgets dans les autres fonctions
dictio = {"batmobile": "Voiture de Batman", 
              "batgrappin": "Grappin de Batman", 
              "batwing": "Avion de Batman",
              "batcostume": "Costume de Batman"}


# BAT FONCTION
# Fct qui prend en paramètre un nom de gadget et renvoie sa description
def analyse_gadget(nom_gadget: str):

    # Vérif si le gadget est dans le dictionnaire (Variable globale qu'on a crée au début)
    if nom_gadget in dictio:
        print(dictio[nom_gadget])

    else:
        print("Ce gadget n'est pas dans la liste")


# BAT REGISTRE
# Fonction qui analyse un fichier et compare le nom des gadgets, comptent le nombre d'occurence des gadgets et ajoute le nombre d'occurence dans un dictionnaire
def count_gadget():
    occurence = {}
    # Ouvrir fichier avec la permission de lecture car on a pas besoin d'écrire mais juste de récupérer les données
    with open("batman_test/bat_registre.txt", "r") as registre:
        gadgets = registre.readlines() # Fonctions qui renvoie une liste en lisant le fichier --> chaque ligne = un gadget 

        for element in gadgets: # Parcourir chaque élément (ligne) de la liste gadgets
            gadget = element.strip().lower() # enlever les espaces et mettre en minuscule pour éviter les doublons (pas sensible à la casse)
            if gadget in occurence:
                occurence[gadget] += 1 # si occurence existe déjà: on ajoute + 1 au compteur
            else:
                occurence[gadget] = 1 # si occurence existe pas encore la crée et lui met 1 au compteur

    print(occurence)


# BAT SIGNAL
# fonction qui dmd à l'utilisateur si il a besoin d'aide, boucle infinie tant qu'il ne termine pas le bouclage avec quit
def bat_signal():
    answer = "" # variable pour stocker la réponse de l'utilisateur et qui permet de vérifier la condition de bouclage

    # Boucle infinie tant que l'utilisateur ne tape pas quit
    while answer != "quit":
        answer = str(input("Avez vous besoin besoin d'aide: oui, non, quit ? "))
        if answer == "oui":
            print("Batman est en route !")
        elif answer == "non":
            print("Gotham est en sécurité pour le moment.")
        elif answer == "quit":
            print("Batman prend une pause café :) ")
        else:
            print("Mauvaise réponse, veuillez envoyer un autre message: ")


# GESTION DES GADGETS
# Fct qui ajoute un gadget dans le dictionnaire
def ajouter_gadget(nom_gadget: str, description: str):

    if nom_gadget not in dictio: # vérifier si le gadget n'est pas déjà dans le dictionnaire
        dictio[nom_gadget] = description # ajouter le gadget dans le dictionnaire
        print("Gadget ajouté avec succès: ")
        print(dictio)
    else:
        print("Ce gadget se situe déjà dans la liste: ") # si le gadget est déjà dans le dictionnaire, on ne dit rien

# Fct qui supprime un gadget du dictionnaire
def supprimer_gadget(nom_gadget: str):

    if nom_gadget in dictio: # Vérifier si le gadget est dans le dictionnaire
        del dictio[nom_gadget] # Si oui, on le supprime
        print(f"Le gadget: {nom_gadget} a été supprimé avec succès")

    else: # Si non, on ne fait rien
        print(f"Ce gadget: {nom_gadget} n'existe pas dans la liste")

# Fct qui modifie la description d'un gadget
def modifier_gadget(nom_gadget: str, nouvelle_description: str):
    if nom_gadget in dictio:
        dictio[nom_gadget] = nouvelle_description
        print(f"La description du gadget: {nom_gadget} a été modifiée avec succès")
    else:
        print(f"Ce gadget: {nom_gadget} n'existe pas dans la liste")

# Fct qui affiche les gadgets
def afficher_gadgets(): # Affiche la clé et la valeur de chaque élément du dictionnaire
    for key, value in dictio.items():
        print(key, "->", value)


# INTERFACE UTILISATEUR, première fonction qui se lance dans le programme
def interface():

    # Print le menu des choix disponibles
    print("Bienvenue dans le menu de Batman")
    print("1. Analyser un gadget")
    print("2. Ajouter un gadget")
    print("3. Supprimer un gadget")
    print("4. Modifier un gadget")
    print("5. Afficher les gadgets")
    print("6. Compter les gadgets dans le bat registre")
    print("7. Bat signal")
    print("8. Quitter")


    # Gestion des erreurs, on vérifie que l'utilisateur rentre bien un nombre entier et pas autre chose (string, float, etc)
    try:
        choix = int(input("Entrez votre choix: "))
        if choix == 1:
            nom_gadget = str(input("Entrez le nom du gadget: "))
            analyse_gadget(nom_gadget)

        elif choix == 2:
            nom_gadget = str(input("Entrez le nom du gadget: "))
            description = str(input("Entrez la description du gadget: "))
            ajouter_gadget(nom_gadget, description)

        elif choix == 3:   
            nom_gadget = str(input("Entrez le nom du gadget: "))
            supprimer_gadget(nom_gadget)

        elif choix == 4:
            nom_gadget = str(input("Entrez le nom du gadget: "))
            nouvelle_description = str(input("Entrez la nouvelle description du gadget: "))
            modifier_gadget(nom_gadget, nouvelle_description)

        elif choix == 5:
            afficher_gadgets()

        elif choix == 6:
            count_gadget()

        elif choix == 7:
            bat_signal()

        elif choix == 8:
            print("Merci d'avoir utilisé le menu de Batman, à bientôt !")
            exit()

        else: # Si l'utilisateur rentre un nombre qui n'est pas dans le menu, on relance l'interface pour qu'il rentre un bon nombre
            print("Mauvais choix, veuillez réessayer: ")
            interface()

    except ValueError: # Si l'utilisateur rentre autre chose qu'un nombre entier, on relance l'interface pour qu'il rentre un bon nombre
        print("Mauvaise valeur, veuillez réessayer en mettant un nombre entier entre 1 et 8: ")
        interface()



# LANCEMENT DE L'INTERFACE
if __name__ == '__main__':
    interface()



