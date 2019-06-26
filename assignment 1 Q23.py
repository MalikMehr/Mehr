# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 03:55:04 2019

@author: MalikMehrKhan
"""
n = input("Enter no. ")
i = 1

while i <= int(n):
    j = 0
    while j != i-1:
        print (i, end = "")
        j += 1
    print (i)
    i += 1
