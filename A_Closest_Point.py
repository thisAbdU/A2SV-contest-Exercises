for _ in range(int(input())):
    n = int(input())
    pts = list(map(int, input().split()))

    if len(pts) > 2:
        print("NO")
    else:
        pts.sort()
        if pts[1] - pts[0] == 1:
            print("NO")
        else:
            print("YES")
