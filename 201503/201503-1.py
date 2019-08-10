m,n = list(map(int,input().split()))
l = []
for i in range(m):
    tem = list(map(int,input().split()))
    l.append(tem)

for j in range(n-1,-1,-1):
    for i in range(m):
        print(l[i][j],end = ' ')
    print("")
