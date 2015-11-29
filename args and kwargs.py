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

#podsumowując argi i kwargi można używać w deklaracji funkcji lub przy wywoływaniu

# przy deklaracji args - możemy do funkcji wrzucić dowolną ilość
# elementów nie będących słownikiem

# przy deklaracji kwargs - możemy do funkcji wrzucić dowolną ilość
# słowników - kluczy i values

# jesli używamy *parameter to potem odwołujemy się do wszystkich elementów
# przez pętle

# jeśli używamy **parametr to potem sprawdzamy czy parameter nie jest pusty
# jeśli nie, wykonujemy pętle for k,v in  parametr.iteritems()
# i uzyskujemy dostęp do kluczy i wartosci :)

# jesli uzywamy przy wywoływaniu funkcji to w celu póżniejszego
# wrzucenia jednej zmiennej (**klucz/wartosc i *wartosciNieDicty)
# do funkcji która robi za to wszystko np:
# args = 1,2,3
# a(*args)

# skrótowo przy wywoływaniu - szybsze ładowanie wielu elementów

# przy defincji możliwość ładowania wielu elementów **dictów lub *pozostałych
