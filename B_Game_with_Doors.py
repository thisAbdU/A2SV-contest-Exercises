for _ in range(int(input())):
    al, ar = list(map(int, input().split()))
    bl, br = list(map(int, input().split()))

    st = min(al, bl)
    end = max(ar, br)

    pt = [0 for i in range(end + 1)]

    for i in range(al, ar + 1):
        pt[i] += 1

    for i in range(bl, br + 1):
        pt[i] += 1

    cnt = 0
    for i in range(1, len(pt)):
        if pt[i] + pt[i - 1] == 3 or pt[i] + pt[i - 1] == 4:
            cnt += 1

    print(max(1, cnt))
        

    

