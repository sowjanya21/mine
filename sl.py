# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:25:53 2020

@author: SREE
"""

sum=0
while sum<100:
    d=int(input('roll the dice'))
    if d>0 and d<7:
        temp=sum+d
        if temp<=100:
            sum=temp
        if sum==100:
            print('you won')
    else:
        print('roll it again')

class Snake:
    