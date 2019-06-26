# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 01:34:30 2019

@author: MalikMehrKhan
"""
l = input("Enter letter ")
vovels = ["a", "e", "i", "o", "u"]
l = l.lower()
for t in vovels:
    if t == l:
        print (l + " is a vovel")
        a = t
        break
if a != l:
    print ("sorry not a vovel")
    