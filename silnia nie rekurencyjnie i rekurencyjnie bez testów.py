# -*- coding: cp1250 -*-
__author__ = 'Piotr'
import doctest
import unittest

def fibo(n):
    if n==1 or n==2:
        return  n
    return fibo(n-1)+fibo(n-2)


def fibo2(n):
    a,b = 1,1
    z = []
    for i in range(1,n):
        a,b = b,a+b
        print(a)
        z.append(a)
    return z


z = 1
y = 1
n = 5
for i in range(1,n+1):
    z,y = i*z,z*y+i
print(z)


