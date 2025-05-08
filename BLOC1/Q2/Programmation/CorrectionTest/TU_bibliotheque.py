import unittest
from bibliotheque import bibliotheque

class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        self.bibliotheque = bibliotheque()

    def test_emprunter_livre_succes(self):
        result = self.bibliotheque.emprunter_livre("Savoir coder en 2h", "Alice")
        expected = "Alice a emprunté Savoir coder en 2h."
        self.assertEqual(result, expected)

    def test_emprunter_livre_inconnu(self):
        result = self.bibliotheque.emprunter_livre("Livre pas dans la liste", "Alice")
        expected = "Livre inconnu !" 
        self.assertEqual(result, expected)

    def test_emprunter_livre_stock_epuise(self):
        self.bibliotheque.stock["Les TU pour les Nuls"] = 0  # Simuler un stock épuisé

        # Simuler l'emprunt d'un livre dont le stock est épuisé
        result = self.bibliotheque.emprunter_livre("Les TU pour les Nuls", "David")
        expected = "Stock épuisé !"
        self.assertEqual(result, expected)
        

    def test_deja_emprunter_livre(self):
        self.bibliotheque.emprunter_livre("Savoir coder en 2h", "Alice") # Simuler un emprunt
        
        # Autre manière de simuler un emprunt
        # self.bibliotheque.emprunts["Alice"] = "Les TU pour les Nuls"

        # Simuler un autre emprunt par le même utilisateur
        result = self.bibliotheque.emprunter_livre("Les TU pour les Nuls", "Alice")
        expected = "Vous ne pouvez emprunter qu'un seul livre à la fois."
        self.assertEqual(result, expected)

    def test_rendre_livre_avec_succes(self):
        self.bibliotheque.emprunter_livre("Savoir coder en 2h", "Alice")
        result = self.bibliotheque.rendre_livre("Savoir coder en 2h", "Alice")
        expected = "Alice a rendu Savoir coder en 2h."
        self.assertEqual(result, expected)

    def test_rendre_livre_sans_emprunt(self):
        result = self.bibliotheque.rendre_livre("Savoir coder en 2h", "Alice")
        expected = "Aucun emprunt en cours pour cet utilisateur."
        self.assertEqual(result, expected)

    def test_rendre_livre_jamais_emprunte(self):
        self.bibliotheque.emprunter_livre("Savoir coder en 2h", "Alice")
        result = self.bibliotheque.rendre_livre("Les TU pour les Nuls", "Alice")
        expected = "Cet utilisateur n'a pas emprunté ce livre."
        self.assertEqual(result, expected)

    def test_verifier_disponibilite_livre_existant(self):
        result = self.bibliotheque.verifier_disponibilite("Savoir coder en 2h")
        expected = True
        self.assertEqual(result, expected)

    def test_verifier_disponibilite_livre_inconnu(self):
        result = self.bibliotheque.verifier_disponibilite("Livre pas dans la liste")
        expected = "Livre introuvable."
        self.assertEqual(result, expected)

    def test_afficher_stock_livre_existant(self):
        result = self.bibliotheque.afficher_stock("Savoir coder en 2h")
        expected = "Il reste 5 exemplaires de Savoir coder en 2h."
        self.assertEqual(result, expected)

    def test_afficher_stock_livre_inexistant(self):
        result = self.bibliotheque.afficher_stock("Livre pas dans la liste")
        expected = "Livre inexistant."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
