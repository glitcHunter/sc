# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

def test_var_args(f_arg, *argv, **kwargs):
    print "first normal arg:", f_arg
    for arg in argv:
        print ("another arg through *argv :", arg)

    if kwargs is not None:
        for keys, values in kwargs.iteritems():
            print(keys,values)
print(test_var_args('1','2','3',a='n'))



def test_args_kwargs(arg1, arg2, arg3):
    print "arg1 or kwargs1:", arg1
    print "arg2 or kwargs2:", arg2
    print "arg3 or kwargs3:", arg3

args = 1,2,3
test_args_kwargs (*args)
    
kwargs = {"arg3": 3, "arg2": "two","arg1":5}

test_args_kwargs(**kwargs)

#podsumowuj�c argi i kwargi mo�na u�ywa� w deklaracji funkcji lub przy wywo�ywaniu

# przy deklaracji args - mo�emy do funkcji wrzuci� dowoln� ilo��
# element�w nie b�d�cych s�ownikiem

# przy deklaracji kwargs - mo�emy do funkcji wrzuci� dowoln� ilo��
# s�ownik�w - kluczy i values

# jesli u�ywamy *parameter to potem odwo�ujemy si� do wszystkich element�w
# przez p�tle

# je�li u�ywamy **parametr to potem sprawdzamy czy parameter nie jest pusty
# je�li nie, wykonujemy p�tle for k,v in  parametr.iteritems()
# i uzyskujemy dost�p do kluczy i wartosci :)

# jesli uzywamy przy wywo�ywaniu funkcji to w celu p�niejszego
# wrzucenia jednej zmiennej (**klucz/wartosc i *wartosciNieDicty)
# do funkcji kt�ra robi za to wszystko np:
# args = 1,2,3
# a(*args)

# skr�towo przy wywo�ywaniu - szybsze �adowanie wielu element�w

# przy defincji mo�liwo�� �adowania wielu element�w **dict�w lub *pozosta�ych
