# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:14:31 2019

@author: MalikMehrKhan
"""
n = input("enter a number ")
n = int(n)
c = []
b = n
while (b != 1) and (b > 0):
    c.append(b % 2)
    b = b // 2
if b == 1:
    c.append(1)
print (c)
