# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:53:01 2020

@author: pc
"""
x = 7/100
a=1-x
c=a

for i in range (1,11):

    c = c*a
    print(c)
    print(i)
print('中奖概率为：', 1-c)