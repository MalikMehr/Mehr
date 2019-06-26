# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:51:31 2019

@author: MalikMehrKhan
"""
x1 = input("Enter x1 ")
x1 = int(x1)
x2 = input("Enter x2 ")
x2 = int(x2)
y1 = input("Enter y1 ")
y1 = int(y1)
y2 = input("Enter y2 ")
y2 = int(y2)
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
f1 = [x1, y1]
f2 = [x2, y2]
print ("The distance between " + str(f1) + " and " + str(f2) + " is " + str(d))

