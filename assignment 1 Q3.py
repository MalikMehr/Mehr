# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:11:16 2019

@author: MalikMehrKhan
"""
numerator = input("Enter numerator value ")
denominater = input("Enter denominater value ")
numerator = int(numerator)
denominater = int(denominater)
remainder = numerator % denominater
if remainder == 0:
    print ("your given numerator is divisible by your given denominater")
else:
    print ("your given numerator in not divisible by your given denominater")

    