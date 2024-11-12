for _ in range(int(input())):
    num = int(input())
    val = {5 : 3, 2 : 1, 3 : 2}
    res = 0

    POSSIBLE = True
    while num != 1:
        if num%5 == 0:
            res += 3
            num //= 5
        elif num%3 == 0:
            res += 2
            num //= 3
        
        elif num%2 == 0:
            res += 1
            num //= 2
        else:
            POSSIBLE = False
            break

    if POSSIBLE:
        print(res)
    else:
        print(-1)