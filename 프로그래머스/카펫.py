a, b = input().split()

brown = int(a)

red = int(b)

answer = []; 

width = brown + red

for i in range(1,int(width/2)):
    if(width % 1 == 0):
        n = i
        m = width/n
        if(n < m):
            continue

        tmp = (n-2) * (m-2)
        tmp2 = width - tmp
        if(tmp == red and tmp2 == brown):
            print(n,m)
            break
