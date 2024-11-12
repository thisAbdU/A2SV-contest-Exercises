def can_reach_destination(n, rows):
    # Initialize lists to check diagonal patterns
    ok1 = [False] * (n // 2)
    ok2 = [False] * (n // 2)


    for i in range(2):
        s = rows[i]
        for j in range(n):
            if (i + j) % 2 == 1:
                if s[j] == '<':
                    ok1[(i + j) // 2] = True
            if (j - i + 1) % 2 == 0:
                if s[j] == '<':
                    ok2[(j - i + 1) // 2] = True

    for i in range(n // 2):
        if ok1[i] and ok2[i]:
            return "NO"
    
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    rows = [input().strip() for _ in range(2)]

    print(can_reach_destination(n, rows))
