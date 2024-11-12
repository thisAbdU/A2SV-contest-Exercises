for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        cols = list(input())
        arr.append(cols)
    
    res = []
    for row in range(n):
        for col in range(4):
            if arr[row][col] == '#':
                res.append(col + 1)
                continue
    
    print(*res[::-1])

