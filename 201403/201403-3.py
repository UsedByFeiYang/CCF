# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:21:37 2019

@author: Administrator
"""
def sort(l,d):
   if l == []:
       return
   l.sort()
   if d == {}:
       return
   for key,values in d.items():
       l.insert(l.index(key)+1,values)
pat = input()
l_pat =list(pat)
i = 0
n = len(l_pat)
while i < n:
    if l_pat[i] == ':':
        l_pat[i-1] += l_pat[i]
        del l_pat[i]
        n = n -1
    i += 1
n = int(input())
for i in range(n):
    ret = []
    d = {}
    s = input().split()
    del s[0]
    j = 0
    flag = 0
    while j < len(s):
        if s[j][0] == '-':
            if s[j][1] in l_pat and s[j] not in ret:
                ret.append(s[j])
                j = j + 1
            elif (s[j][1] + ':' in l_pat) and j+1<len(s) and str.isdigit(s[j+1]) :
                if s[j] not in ret:    
                    ret.append(s[j])
                    d[s[j]] = s[j+1]
                else:
                    d[s[j]] = s[j+1]
                j = j + 2
            else:
                sort(ret,d)
                print('Case {}:'.format(i+1)+' '+ ' '.join(ret))
                flag = 1
                break
        else:
            sort(ret,d)
            print('Case {}:'.format(i+1)+' '+ ' '.join(ret))
            flag = 1
            break
    if flag == 0:
        sort(ret,d)
        print('Case {}:'.format(i+1)+' '+ ' '.join(ret))


        
        