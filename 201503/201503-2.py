n = int(input())
l = list(map(int,input().split()))
d = dict()
for item in l:
    if item not in d.keys():
        d[item] = 1
    else:
        d[item] += 1
ret = sorted(d.items(),key = lambda x:x[0])
ret = sorted(ret,key = lambda x:x[1],reverse = True)
for x,y in ret:
    print(x,y)

