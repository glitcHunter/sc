# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

class recursive_calculate_list_of_number():

    def suma(self,tab):
        if len(tab) ==1:
            return tab[0]
        else:
            return tab[0]+self.suma(tab[1:])
        
convString = "abcd"

def anagramik(a,b):
    if(len(a)!=len(b)):
        return False
    is_okay = True
    while is_okay!=True and i<=len(a):
        for i in range(len(a)):
        
            for j in range(len(b)):

                if a[i]!=b[j]:
                    is_okay = False
        ++i
    return True

def theSame(a,b):

    is_ok = True
    a = list(a)
    b = list(b)

    if len(a)!=len(b):
        return False
    while len(a)>0 and is_ok:

        if a[0] == b[0]:
            a.pop(0)
            b.pop(0)
        else:
            is_ok = False
            return is_ok

    return True    


def palindrom(string):
    string = list(string)

    while len(string)>1:
        if string.pop(0)==string.pop():
            print('dsadas')
        else:
            return False
        
    return True 


print(palindrom('absba'))

#print(theSame('123','124'))
#print(anagramik('sad','das'))

class test_recursive_calculate_list_of_number(unittest.TestCase):

    def setUp(self):
        self.Item = recursive_calculate_list_of_number()
    def test_sums_equals(self):
        self.assertEqual(self.Item.suma([1,2,3,4]),10)
    
if __name__ == "__main__":
    unittest.main()
        

