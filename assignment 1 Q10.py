# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:19:08 2019

@author: MalikMehrKhan
"""
p = input("Enter amount ")
a = int(p)
i = input("Enter the interest in percentage ")
i = int(i)
t = input("Enter number of years ")
t = int(t)
pa = ((a * i * t) / 100) + a
print ("\nthe amount is " + str(pa))
