class bibliotheque:
    def __init__(self):                                     
        self.stock = {
            "Savoir coder en 2h": 5,
            "Les TU pour les Nuls": 3,
            "Réussir ses exams sans étudier": 4
        }
        self.emprunts = {}

    def emprunter_livre(self, livre, utilisateur):          
        if livre not in self.stock:                         
            return "Livre inconnu !"
        
        if self.stock[livre] <= 0:                          
            return "Stock épuisé !"
        
        if utilisateur in self.emprunts:                    
            return "Vous ne pouvez emprunter qu'un seul livre à la fois."
        
        self.stock[livre] -= 1
        self.emprunts[utilisateur] = livre
        return f"{utilisateur} a emprunté {livre}."

    def rendre_livre(self, livre, utilisateur):             
        if utilisateur not in self.emprunts:
            return "Aucun emprunt en cours pour cet utilisateur."
        if self.emprunts[utilisateur] != livre:
            return "Cet utilisateur n'a pas emprunté ce livre."
        
        livre = self.emprunts.pop(utilisateur)
        self.stock[livre] += 1
        return f"{utilisateur} a rendu {livre}."

    def verifier_disponibilite(self, livre):                
        if livre not in self.stock:
            return "Livre introuvable."
        return self.stock.get(livre, 0) > 0

    def afficher_stock(self, livre, stock):
        if livre in stock:
            print(f"il y a actuellement {stock} exemplaires de {livre} en stock \n")
        else:
            print(f"{livre} n'est pas en stock \n")

