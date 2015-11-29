# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

class find_all_elements_from_list_b_in_list_a():
    '''za głupi by pamiętać'''
    
    def find_elements(self, a,b):
        res = [i for i in a if i in b]
        return ''.join(res)    

class tset_find_all(unittest.TestCase):

    def test_find_all_elements_from_list_b_in_list_a(self):
        '''to jest ciekawe, jeśli bym zwracał res to by był błąd
        ponieważ otrzymałem [res] zamiast 'res' użyłem join aby przekonwertować
        na str'''

        item = find_all_elements_from_list_b_in_list_a()
        a = ["mp3","a"]
        b = ["mp3"]
        self.assertEqual(item.find_elements(a,b),"mp3")
        
    
if __name__ == "__main__":
    unittest.main()
        

