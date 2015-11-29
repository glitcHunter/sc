# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

from random import randint



def addOne(mFunc):
    def addOneInside(*args,**kwargs):
        return mFunc(*args,**kwargs)+1
    return addOneInside


@addOne
def odFunc(x = 321):
    return x


print(odFunc(421))




def decFunction(sandwich):
    def ham(*args, **kwargs):
        return "ham"+sandwich(*args, **kwargs)
    return ham

@decFunction
def sandwich():
    return "sandwich" 

print(sandwich())



def dec2Function(losowanie):
    def dodatek(*args, **kwargs):
        return losowanie(*args, **kwargs)
    return dodatek


@dec2Function
def losowanie():
    return randint(0,9)

print(losowanie())




