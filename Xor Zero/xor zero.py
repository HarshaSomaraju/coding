import math
t = int(input())

for i in range(t):
    n = int(input())
    flag = 0

    if n%2 == 1:
        print('-1')
        continue
    c = n//2
    if c%2 == 1:
        a = 1
        b = c-1
        if (a^b) == c:
            print(a,b,c)
        else:
            print('-1')
    else:
        power = 0
        end = int(math.log2(c))
        for p in range(power, end):
            a = int(2**p)
            b = c-a
            if (a^b) == c:
                print(a,b,c)
                flag=1
                break
        if flag==0:
            print('-1')