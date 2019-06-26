# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:57:34 2019

@author: MalikMehrKhan
"""
a = []
b = "yes"
while b != "no":
    b = input("Enter each term even space induvidually and press no to finish ")
    b = b.lower()
    if b != "no":
        a.append(b)
c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
d = " "
e = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = 0
space = 0
symbols = 0
number = 0
for x in a:
    for t in c:
        if t == x:
            alphabet += 1            
for x in a:
    for z in e:
        if x == z:
            number += 1
for x in a:
    if x == d:
        space += 1
symbols = len(a) - number - space - alphabet
print (a)
print ("the alphabets are " + str(alphabet) )
print ("the numbers are " + str(number))
print ("the spaces are " + str(space))
print ("the special characters are " + str(symbols))            
    
        
