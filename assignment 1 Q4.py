# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:19:21 2019

@author: MalikMehrKhan
"""
print ("Format is date 1 - date 2")
a = "no"
while a != "yes":
    D1 = int(input("Enter D1 "))
    D2 = int(input("Enter D2 "))
    M1 = int(input("Enter M1 "))
    M2 = int(input("Enter M2 "))
    Y1 = int(input("Enter Y1 "))
    Y2 = int(input("Enter Y2 "))
    print ("your Date 1 = " + str(D1) +"/" + str(M1) + "/" + str(Y1))
    print ("your Date 2 = " + str(D2) +"/" + str(M2) + "/" + str(Y2))
    a = input("If fine press yes and if wrong press no ")               
f = 28
a = 31
b = 30 
x = 0
s = 0                  
if Y1 > Y2:
    n = Y1 - Y2 
    if M2 == 2:
        x = f + (4 * b) + (6 * a)
    elif M2 == 1:
        x = f + (4 * b) + (7 * a)
    elif M2 == 3:
        x = (4 * b) + (6 * a)
    elif M2 == 4:   
        x = (4 * b) + (5 * a)
    elif M2 == 5:
        x = (3 * b) + (5 * a)
    elif M2 == 6:
        x = (3 * b) + (4 * a)
    elif M2 == 7:
        x = (2 * b) + (4 * a)
    elif M2 == 8:
        x = (2 * b) + (3 * a)
    elif M2 == 9:
        x = (2 * b) + (2 * a)
    elif M2 == 10:
        x = b + (2 * a)
    elif M2 == 11:
        x = b + a
    elif M2 == 12:
        x = a
    x = x + ((n-1) * 365)
    M2 = 1
    if D2 > 1:
        q = D2 - 1
        D2 = 1
    if M1 == 2:
        s = a
    elif M1 == 3:
        s = a + f
    elif M1 == 4:   
        s = a + f + a
    elif M1 == 5:
        s = a + f + a + b
    elif M1 == 6:
        s = a + f + a + b + a
    elif M1 == 7:
        s = a + f + a + b + a + b
    elif M1 == 8:
        s = a + f + a + b + a + b + a
    elif M1 == 9:
        s = a + f + a + b + a + b + a + a
    elif M1 == 10:
        s = a + f + a + b + a + b + a + a + b
    elif M1 == 11:
        s = a + f + a + b + a + b + a + a + b + a
    elif M1 == 12:
        s = a + f + a + b + a + b + a + a + b + a + b
if Y2 == Y1:
    if D2 > 1:
        q = D2 - 1
        D2 = 1
    if M2 == 2:
         s = - f
    elif M2 == 3:
         s = - f - a
    elif M2 == 4:
         s = - f - a - b
    elif M2 == 5:
         s = - f - a - b - a
    elif M2 == 6:
         s = - f - a - b - a - b
    elif M2 == 7:
         s = - f - a - b - a - b - a
    elif M2 == 8:
         s = - f - a - b - a - b - a - a
    elif M2 == 9:
         s = - f - a - b - a - b - a - a - b
    elif M2 == 10:
         s = - f - a - b - a - b - a - a - b - a
    elif M2 == 11:
         s = - f - a - b - a - b - a - a - b - a - b
    elif M2 == 12:
         s = - f - a - b - a - b - a - a - b - a - b - a
    if M1 == 2:
        s = s + a
    elif M1 == 3:
        s = s + a + f
    elif M1 == 4:   
        s = s + a + f + a
    elif M1 == 5:
        s = s + a + f + a + b
    elif M1 == 6:
        s = s + a + f + a + b + a
    elif M1 == 7:
        s = s + a + f + a + b + a + b
    elif M1 == 8:
        s = s + a + f + a + b + a + b + a
    elif M1 == 9:
        s = s + a + f + a + b + a + b + a + a
    elif M1 == 10:
        s = s + a + f + a + b + a + b + a + a + b
    elif M1 == 11:
        s = s + a + f + a + b + a + b + a + a + b + a
    elif M1 == 12:
        s = s + a + f + a + b + a + b + a + a + b + a + b
U = D1 - D2 - q
total = x + s + U
print ("Total days spent = " + str(total))
print (s)
print (x)
print (U)
   
        

        