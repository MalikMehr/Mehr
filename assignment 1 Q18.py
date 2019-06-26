# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:21:50 2019

@author: MalikMehrKhan
"""
w = "9"
b = []
while w != "no":
    w = input("Enter letters of the text ")
    w = w.lower()
    if w != "no" and w != "9":
        b.append(w)
v = 0
c = 0
for t in b:
    if t == "a":
        v += 1
    elif t == "e":
        v += 1
    elif t == "i":
        v += 1
    elif t == "o":
        v += 1
    elif t == "u":
        v += 1
    else:
        c += 1
print ("Vovels are =" + str(v) + " and consonants are =" + str(c))
    
