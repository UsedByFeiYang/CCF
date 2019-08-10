# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:10:26 2019

@author: Administrator
"""

n,m = list(map(int,input().split()))
l = []
for i in range(1,n+1):
    ltem = []
    ltem.extend(list(map(int,input().split())))
    ltem.append(i)
    l.append(ltem)

l = l[-1::-1]
for i in range(m):
    x,y = list(map(int,input().split()))
    j = 0
    for x1,y1,x2,y2,i in l:
        if x >= x1 and x <= x2 and y >=y1 and y <=y2:
            print(i)
            l.insert(0,l[j])
            del l[j+1]
            break
        else:
            j += 1
    if j == len(l):
        print("IGNORED")
