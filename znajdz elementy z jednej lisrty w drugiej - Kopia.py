# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

class find_all_elements_from_list_b_in_list_a():
    '''za g�upi by pami�ta�'''
    
    def find_elements(self, a,b):
        res = [i for i in a if i in b]
        return ''.join(res)    

class tset_find_all(unittest.TestCase):

    def test_find_all_elements_from_list_b_in_list_a(self):
        '''to jest ciekawe, je�li bym zwraca� res to by by� b��d
        poniewa� otrzyma�em [res] zamiast 'res' u�y�em join aby przekonwertowa�
        na str'''

        item = find_all_elements_from_list_b_in_list_a()
        a = ["mp3","a"]
        b = ["mp3"]
        self.assertEqual(item.find_elements(a,b),"mp3")
        
    
if __name__ == "__main__":
    unittest.main()
        

