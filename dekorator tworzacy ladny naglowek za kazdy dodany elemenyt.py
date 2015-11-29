# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest


def decorator(naglowek):
    def dodatek(*args,**kwargs):
        templecik = ''
        for i in naglowek('Super','Niesłychane',"10/10"):
            
            templecik += '.::'+i+'::. '
            
        return('*'*len(templecik)+'\n'+templecik+'\n'+'*'*len(templecik))
    return dodatek

@decorator

def naglowek(*args):
    concat =''
    for i in args:
        concat=i 

        yield concat


print(naglowek())



