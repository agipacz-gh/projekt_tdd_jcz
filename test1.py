import unittest
import moj_program #krok 1: tego jeszcz nie ma. dopiero to napisze; krok 2: tworze plik moj_program.py i tam zwracam wartosc 100;

class Test1TDD(unittest.TestCase):

    def test_100(self):
        wynik = moj_program.zwroc_100()
        self.assertEqual(100, wynik) #porownuje jedna warosc do drugiej czyli 100 z tym naszym wynikiem

    def test_zwroc_parametr(self):
        ret = moj_program.zwroc_parametr('asia')
        self.assertEqual(ret, 'asia')


if __name__ == '__main__':
    unittest.main()
