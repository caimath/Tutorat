
# Doctor Who - L'exam blanc

'''
Réalisé par: Mathias Carsault
Le but de cet examen est de montrer que tu connais les bases de python et que tu sais les appliquer.

Comment gagner des points ? En leur montrant ce que tu sais faire: Ouverture de fichier, boucle, condition, fonction, dictionnaire,...

- Avoir une syntaxe commune pour la déclaraiton  de variable (CamelCase, "_" pour séparer,...)
- Quand tu ouvres un fichier, il faut bien le refermer après utilisation.
- Tu dois coder une fonction pour chaque paragraphe en général.
- Essayer de gérer les erreurs que l'utilisateur pourrait faire et essayer d'envisager tout les cas (utilisaion de try except et if elif else), si il rentre une mauvaise valeur, tu dois lui redemander de rentrer une valeur correcte.
- Le code ne doit surtout pas planter, d'où le but de gérer les erreurs et les entrées de l'utilisateur.
- Éviter les boucles infinies, sauf si c'est nécessaire. Dans ce cas ci, c'est nécessaire dans la fonction "L'appel à l'aide" (demandé dans l'énoncé).
- Commenter ton code pour expliquer ce que tu fais.
- Faire des tests unitaires (Pas fait ici, mais je les ferai peut-être plus tard, si besoin, il y a un exemple d'utilisation de test unitaire dans https://github.com/caimath/Tutorat/blob/main/BLOC1/Q1/Programmation/Batman/main.py )

J'ai beaucoup moins commenté ce code que celui de l'examen "Batman". Si tu veux plus d'explications, n'hésite pas à me contacter ou à d'abord faire l'examen batman.

Me contacter: 
Mail: mathias.carsault@std.heh.be
Github: https://github.com/caimath
'''

# Dictionnaire des compagnons du docteur
dictio_compagnon = {"gregy":"tutoré",
                    "mathias" : "Tutorat",
                    "Depreter" : "va me tuer avec ces examens de fou furieux"}


# LES COMPAGNONS DU DOCTEUR
def analyser_compagnon(nom:str):
    if nom in dictio_compagnon:
        print(dictio_compagnon[nom])
    else:
        print(f"Le compagnon: {nom}, n'est pas présent dans le dictionnaire")

# SCAN DE COMPAGNON
def scan_compagnon(nom:str):

    # Si le compagnon est présent dans le dictionnaire, on propose de modifier sa description
    if nom in dictio_compagnon:
        print("Le compagnon est présent")
        choix_descri = str(input("Voulez-vous changer la description du compagnon? Tapez 'Oui' ou 'Non'"))

        # Proposition de modifier la description
        if choix_descri.lower() == "oui":
            description_compagnon = str(input("Veuillez décrire le compagnon: "))
            dictio_compagnon[nom] = description_compagnon
            print(f"La description de {nom} a été modifiée avec succès: {description_compagnon}")
        else:
            print(f"La description de {dictio_compagnon[nom]} n'a pas été modifiée")

    # Si le compagnon n'est pas présent dans le dictionnaire, on l'ajoute et demande de rentrer une description
    else:
        description_compagnon = str(input("Veuillez décrire le compagnon: "))
        dictio_compagnon[nom] = description_compagnon
        print(f"Le compagnon {nom} a été ajouté avec succès avec la description: {description_compagnon}")

# LE REGISTRE DU TARDIS
def lire_registre():

    # Créer une variable pour stocker le nombre d'occurence
    nbr_occurence = {}

    # Ouvrir le fichier en mode lecture
    with open("registre.txt", "r") as f:
        contenu = f.readlines()

        # Parcourir le fichier ligne par ligne
        for ligne in contenu:
            ligne = ligne.strip().lower()

            if ligne != "missy": # ATTENTION: LE MAÎTRE S'EN CHARGE --> Exclure missy du comptage des compagnons
                if ligne in nbr_occurence:
                    nbr_occurence[ligne] += 1
                else:
                    nbr_occurence[ligne] = 1
    print("Voici le registre du TARDIS : \n", nbr_occurence)
   
# L'APPEL A L'AIDE
def appel_aide():
    reponse = "" # Initialise une variable vide pour la condition de la boucle while

    # Boucle infinie
    while reponse.lower() != "quit":
        
        # Demande à l'utilisateur s'il veut appeler à l'aide
        # .strip() pour supprimer les espaces et .lower() pour mettre en minuscule --> Pour éviter la casse
        reponse = input("Voulez-vous appeler à l'aide? Tapez 'Oui', 'Non' ou 'quit' pour quitter l'appel à l'aide.").strip().lower() 

        if reponse== "oui":
            print("Le docteur arrive !")
        elif reponse == "non":
            print("L'Humanité est en sécurité pour le moment")
        else:
            print("Veuillez mettre 'Oui', 'Non' ou 'Quit'")
    print("Fin de l'appel à l'aide")

# INTERFACE 
def interface():

    # Afficher tout les choix possibles
    print("Bienvenue dans le programme Doctor Who !")
    print("Que voulez-vous faire?")
    print("1. Analyser un compagnon")
    print("2. Scanner un compagnon")
    print("3. Lire le registre du Tardis")
    print("4. Appeler à l'aide")
    print("5. Quitter le programme")

    # Utilisation de try except pour gérer les erreurs de l'utilisateur
    try:
        choix = int(input("Veuillez choisir un chiffre entre 1 et 5: "))
        if choix == 1:
            nom = str(input("Veuillez entrer le nom du compagnon: "))
            analyser_compagnon(nom)
        elif choix == 2:
            nom = str(input("Veuillez entrer le nom du compagnon: "))
            scan_compagnon(nom)
        elif choix == 3:
            lire_registre()
        elif choix == 4:
            appel_aide()
        elif choix == 5:
            print("Merci d'avoir utilisé le programme Doctor Who !")
            exit() # Quitter le programme proprement
        else:
            print("Veuillez entrer un chiffre entre 1 et 5")
            interface()

    except ValueError:
        print("Veuillez entrer un chiffre entre 1 et 5 et pas autre chose")
        interface()

# LANCEMENT DU PROGRAMME
if __name__ == "__main__":
    interface()
    print("Merci d'avoir utilisé le programme Doctor Who !")

# FIN DU PROGRAMME