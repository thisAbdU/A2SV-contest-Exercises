def can_shower(inter, m, d):
    inter.sort()
    
    if inter[0][0] - 0 >= m or d - inter[-1][1] >= m:
        return "YES"
    
    for i in range(1, len(inter)):
        if inter[i][0] - inter[i-1][1] >= m:
            return "YES"
        
    return "NO"


for _ in range(int(input())):
    n, m, d = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        a, b  = list(map(int, input().split()))
        arr.append((a, b))

    print(can_shower(arr, m, d))