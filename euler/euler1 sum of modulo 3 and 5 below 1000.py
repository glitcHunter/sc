# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

class euler1():

    
    def euler1below1000(self, N=1000):

        if N>1000:
            raise(ValueError)    
        if(N>2):
            result = ([i for i in range(2,N) if i%3==0 or i%5==0])
            return (sum(result))
        elif N<=2:
            return 0
        
    
class Testeuler1(unittest.TestCase):

    def setUp(self):
        self.Item = euler1()


    def test_euler1(self):
        self.Item.euler1below1000(15)

    def test_raise_euler1(self):
        with self.assertRaises(ValueError):
            self.Item.euler1below1000(1001)

    def test__N_less_than_3_0_euler1(self):
        self.assertEqual(self.Item.euler1below1000(2),0)

    def test_good_euler1(self):
        self.assertEqual(self.Item.euler1below1000(15),45)
        
    
if __name__ == "__main__":
    unittest.main()
        

