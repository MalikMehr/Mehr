# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:28:46 2019

@author: MalikMehrKhan
"""
a = 0
b = []
c=[]
while (a == 1) or (a == 0):
    a = input("Enter binary digit ")
    a = int(a)
    if a == 1 or a == 0:
        b.append(a)
n = len(b) - 1
for x in b:
    c.append(x * 2**n)
    n = n - 1
d = sum(c)
print ("decimal number is " + str(d))
