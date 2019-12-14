import unittest
import powitanie

class testy_hello(unittest.TestCase):

    def test_powitanie(self):
        wynik = powitanie.zwroc_hello()
        self.assertEqual("Hello World", wynik)

        print(wynik)

if __name__ == '__main__':
    unittest.main()
