# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 08:52:33 2019

@author: Administrator
"""

n = int(input())
x = list(map(int,input().split()))
x = [abs(item) for item in x]
d = dict()
for item in x:
    if item not in d.keys():
        d[item] = 1
    else:
        d[item] += 1
count = 0
for value in d.values():
    if value == 2:
        count += 1
print(count)