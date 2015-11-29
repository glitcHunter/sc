__author__ = 'Piotr'
import unittest
import doctest

class proste_generatory():
    def wygeneruj_parzyste(self,N):
        for i in range(N):
            if i%2 ==0:
                yield i #zwracanie obiektu generatora


Item = proste_generatory()

# o generatoach:
# 1 - zwracaj¹ obiekt generatora
# 2 - u¿ywaj¹ s³ówka kluczowego yield do zwrócenia obiektu
# 3 - nie mo¿na ³¹czyæ return i yield, po u¿yciu yield funckja jest generatorem
# 4 - aby przechodziæ po nastêpnych wartoœciach generatora nale¿y u¿yæ funkcja_generatora.next()
# 5 - yield nie koñczy funkcji  jak return
# 6 - nie mo¿na u¿ywaæ try catch z s³ówkiem yield

class test_proste_generatory(unittest.TestCase):

    def setUp(self):
        self.Item = proste_generatory()

    def test_proste_last_element(self):
        test=0
        for i in Item.wygeneruj_parzyste(21):
            test = i
        self.assertEqual(test,20)

    def test_proste_first_element(self):
        self.assertEqual(self.Item.wygeneruj_parzyste(21).next(),0)

    
        

if __name__ =='__main__':
    unittest.main()









