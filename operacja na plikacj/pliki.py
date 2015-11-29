import unittest
'''

r	Opens a file for reading only.
The file pointer is placed at the beginning of the file.
This is the default mode.
rb	Opens a file for reading only in binary format.
The file pointer is placed at the beginning of the file.
This is the default mode.
r+	Opens a file for both reading and writing.
The file pointer placed at the beginning of the file.
rb+	Opens a file for both reading and writing in binary format.
The file pointer placed at the beginning of the file.
w	Opens a file for writing only.
Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb	Opens a file for writing only in binary format.
Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
w+	Opens a file for both writing and reading.
Overwrites the existing file if the file exists.
If the file does not exist, creates a new file for reading and writing.
wb+	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
ab	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
ab+	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''
class operacjeNaPlikach():

    def tworzenie_i_zapis_do_pliku(self,nazwa_pliku,typ):
        if type(nazwa_pliku) != str:
            nazwa_pliku = 'test'
            raise(ValueError)
        
        nowy_plik =nazwa_pliku+ typ
        
        plik = open(nowy_plik,'a')
        plik.write('tresc')
        plik.close()    
        return nowy_plik

    def usuniecie_zawartosci_tego_pliku(self):
        pass
        

Item = operacjeNaPlikach()

Item.tworzenie_i_zapis_do_pliku('odczyt','.txt',)

plik  = open('a.txt', 'a')
plik.write('ada')
plik.close()



lista = ['1','2','3',str(5)]

plik = open('plik', 'w')
plik.writelines(lista)
plik.close()


zrodlo = open('plik','w').readlines()




class test_operacjeNaPlikach(unittest.TestCase):

    def setUp(self):
        self.Item = operacjeNaPlikach()

    def test_tworzenie_i_zapis_do_pliku(self):
        self.assertEqual(self.Item.tworzenie_i_zapis_do_pliku('odczyt','.txt'),'odczyt.txt')

    def test_raise_tworzenie_pliku(self):
        with self.assertRaises(ValueError):
            self.Item.tworzenie_i_zapis_do_pliku([2],'.txt')
    


if __name__ == '__main__':
    unittest.main()
    
