import unittest
from bibliotheque import bibliotheque

class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        pass

    def test_emprunter_livre_succes(self):
        pass

    def test_emprunter_livre_inconnu(self):
        pass

    def test_emprunter_livre_stock_epuise(self):
        pass

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