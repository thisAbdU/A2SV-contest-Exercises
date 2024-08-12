for _ in range(int(input())):
    x, y, k = list(map(int, input().split()))
    nedx = []
    nedy = []

    for i in range(1, k//2 +1):
        nedx.append(x-i)
        nedx.append(x+i)
        nedy.append(y-i)
        nedy.append(y+i)
    if k%2 == 1:
        nedy.append(y)
        nedx.append(x)

    for i in range(k):
        print(nedx[i], nedy[i])
    

