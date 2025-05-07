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
        result = self.bibliotheque.emprunter_livre("Les TU pour les Nuls", "David")
        expected = "Stock épuisé !"
        self.assertEqual(result, expected)
        

    def test_deja_emprunter_livre(self):
        pass

    def test_rendre_livre_avec_succes(self):
        pass

    def test_rendre_livre_sans_emprunt(self):
        pass

    def test_rendre_livre_jamais_emprunte(self):
        pass

    def test_verifier_disponibilite_livre_existant(self):
        pass

    def test_verifier_disponibilite_livre_inconnu(self):
        pass

if __name__ == '__main__':
    unittest.main()
