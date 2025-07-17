import unittest
from aufgabe import Bankkonto

class TestBankkonto(unittest.TestCase):
    def test_konstruktor(self):
        konto = Bankkonto("Max")
        self.assertEqual(konto.inhaber, "Max")
        self.assertEqual(konto.kontostand, 0)

    def test_einzahlen(self):
        konto = Bankkonto("Max")
        konto.einzahlen(100)
        self.assertEqual(konto.kontostand, 100)

    def test_abheben_erfolgreich(self):
        konto = Bankkonto("Max")
        konto.einzahlen(100)
        erfolg = konto.abheben(50)
        self.assertTrue(erfolg)
        self.assertEqual(konto.kontostand, 50)

    def test_abheben_fehlgeschlagen(self):
        konto = Bankkonto("Max")
        erfolg = konto.abheben(50)
        self.assertFalse(erfolg)
        self.assertEqual(konto.kontostand, 0)

    def test_gib_kontostand(self):
        konto = Bankkonto("Max")
        konto.einzahlen(75)
        self.assertEqual(konto.gib_kontostand(), 75)

if __name__ == "__main__":
    unittest.main()
