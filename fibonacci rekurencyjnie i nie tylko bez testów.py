# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest


class fiboTest(unittest.TestCase):

    def setUp(self):
        self.Item = fiboMethods()

    def test_fibo1(self):
        self.assertEqual(self.Item.fibo1(6),13)
    
    def test_fibo2(self):
        self.assertEqual(self.Item.fibo2(6),13)

    def test_fibo1_equal_fibo2(self):
        self.assertEqual(self.Item.fibo1(6),self.Item.fibo2(6))

class fiboMethods():
    
    def fibo1(self,n):
        if n==1 or n==2:
            return  n
        return self.fibo1(n-1)+self.fibo1(n-2)


    def fibo2(self,n):
        a,b = 1,2
        for i in range(1,n):
            a,b = b,a+b
        return a


if __name__ == '__main__':
    unittest.main()
