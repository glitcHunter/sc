__author__ = 'Piotr'
import math
import unittest

class BinaryCode():

    def binary(self,n):

        if type(n) == int:
            n = str(n)
        if type(n)==float:
            n = str(int(n))
        s = list(n)
        s =s[::-1]
        res = 0
        for i in range(0,len(s)):
            res += int(s[i]) * math.pow(2,i)
        return int(res)


    def dec_to_bin(self,x):
        '''bin zamienia liczbe na format 0bwartosc binarna
            np: 0b11 trzeba to odczytaæ jako int oraz pomin¹æ 2 pierwsze elementy
            czyli 0b dlatego [2:]'''
        if type(x) == str or float:
            x = int(x)
        
        return int(bin(x)[2:]) 



class tests_BinaryCode(unittest.TestCase):
    def setUp(self):
        self.Item = BinaryCode()
        
    def test_binary(self):
        self.assertEqual(self.Item.binary(11),3)

    def test_dec_to_bin(self):
        self.assertEqual(self.Item.dec_to_bin(3),11)


if __name__ == '__main__':
    unittest.main()

#print(a[2:])
#print(z)

#print (dec_to_bin(5))
