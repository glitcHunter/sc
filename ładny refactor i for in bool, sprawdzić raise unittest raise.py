__author__ = 'Piotr'
import unittest

class easy():

    def easy_refactor_if_tab_lower_than_len(self,tab):
        if type(tab) != list:
            raise(ValueError)
                        
        if False in [i>=5 for i in tab ]:
            return False
        return True 

class test_easy(unittest.TestCase):

    def test_easy_refactor(self):
        item = easy()
        
        self.assertEqual(item.easy_refactor_if_tab_lower_than_len([21,5,22]),True)

        self.assertEqual(item.easy_refactor_if_tab_lower_than_len([21,1,22]),False)


    def test_easy_raises(self):
        item = easy()
        with self.assertRaises(ValueError):
            item.easy_refactor_if_tab_lower_than_len('')
       
       # self.assertRaises(AssertionError, item.easy_refactor_if_tab_lower_than_len([3]))

if __name__ =='__main__':
    unittest.main()
