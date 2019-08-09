a,b,c,y1,y2 = list(map(int,input().split()))
def IsrunNian(y):
    if y %400 == 0:
        return True
    elif y % 4 == 0 and y % 100 !=0 :
        return True
    else:
        return False

bigM = [1,3,5,7,8,10,12]
smallM = [4,6,9,11]

def judge(a,b,c,y):
    sumday = 0
    r = 0
    for i in range(1850,y):
        if IsrunNian(i):
            sumday += 366
        else:
            sumday += 365
    r = sumday % 7
    r = (2+r)%7
    mday = 0
    for i in range(1,a):
        if i in bigM:
            mday += 31
        elif i in smallM:
            mday += 30
        else:
            if IsrunNian(y):
                mday += 29
            else:
                mday += 28
    r = sumday + mday + 2  # a月1号是星期r
    r = r % 7
    if r == 0:
        r = 7
    if c - r >= 0: 
        day = (c - r) + (b-1)  * 7
    else:
        day = (c - r) + b  * 7

        
    if a in bigM:
        if day + 1 >31:
            print('none')
        else:
            print("{0}/{1:0>2}/{2:0>2}".format(y,a,day+1))
    elif a in smallM:
        if day + 1 >30:
            print('none')
        else:
            print("{0}/{1:0>2}/{2:0>2}".format(y,a,day+1))
    else:
        if IsrunNian(y):
            if day + 1 >29:
                print('none')
            else:
                print("{0}/{1:0>2}/{2:0>2}".format(y,a,day+1))
        else:
            if day + 1 >28:
                print('none')
            else:
                print("{0}/{1:0>2}/{2:0>2}".format(y,a,day+1))


if y1 < y2:
    for i in range(y1,y2+1):
        judge(a,b,c,i)

else:
    for i in range(y2,y1+1):
        judge(a,b,c,i)
