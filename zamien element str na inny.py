import unittest

class test_ATCG(unittest.TestCase):

    def test_dna_to_rna_upper(self):
        item_test = EasyScripts()
        self.assertNotEqual(item_test.dna_to_rna('atcg'),'ATCG'
        ,'blad nie zamienia malych liter na duze')

    

class EasyScripts():
    def dna_to_rna(self,atcg):
        atcg = atcg.upper()
        rna = [i.replace('T','U') for i in atcg]
        return  ''.join(rna)

item = EasyScripts()
print(item.dna_to_rna('atcg'))


if __name__ == '__main__':
    unittest.main()



