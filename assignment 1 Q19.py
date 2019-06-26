# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:57:24 2019

@author: MalikMehrKhan
"""
a = []
b = []
c = "9"
l = 1
z = 1
while c != "no":
    c = input("Enter letters and press no to finish ")
    c = c.lower()
    if c != "no" and c != "9":
        a.append(c)
for t in a:
    b.insert(0, t)
print (a)
print (b)
while l < len(a):
    if a[l - 1] == b[l - 1]:
        z += 1
    l += 1
if z == l:
    print ("palindrome")
else:
    print ("not a palindrome")