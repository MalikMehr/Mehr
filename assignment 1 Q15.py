# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:13:42 2019

@author: MalikMehrKhan
"""
a = []
b = 0
while b != "y":
    b = input("Enter didit of a number and press y to quit ")
    if b != "y":
        b = int(b)
        a.append(b)
        b = str(b)
print (a)
print (sum(a))
        
