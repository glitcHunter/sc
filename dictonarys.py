# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

class my_dictonaries():

    def delete_dykta(self,dyc):
        if type(dyc)!=dict:
            raise(ValueError)
        del dyc

    def peek_dykta_Values(self,dyc):
        if type(dyc)!=dict:
            raise(ValueError)
        
        return dyc.values()

    def peek_dykta_Keys(self,dyc):
        if type(dyc)!=dict:
            raise(ValueError)
        
        return dyc.keys()

class unittests_my_dictonaries(unittest.TestCase):
    
    def test_raises_bad_type_delete_dykta(self):
        Item = my_dictonaries()
        with self.assertRaises(ValueError):
            Item.delete_dykta('')

    def test_raises_bad_type_peek__dykta(self):
        Item = my_dictonaries()
        with self.assertRaises(ValueError):
            Item.peek_dykta_Values('')
            
    def test_del_dykta(self):
        Item = my_dictonaries()
        
        self.assertEqual(Item.delete_dykta({1:1}),None)
                
    def test_peek_dykta_Values(self):
        Item = my_dictonaries()
        dic = {1:1}
        self.assertEqual(Item.peek_dykta_Keys(dic),[1])

    def test_raises_dykta_Values(self):
        Item = my_dictonaries()
        dic = {1:1}
        self.assertEqual(Item.peek_dykta_Values(dic),[1])

    def test_peek_dykta_Keys(self):
        Item = my_dictonaries()
        dic = {1:1}
        self.assertEqual(Item.peek_dykta_Keys(dic),[1])
            
if __name__ == "__main__":
    unittest.main()
        

