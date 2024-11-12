for _ in range(int(input())):
    s, t = list(input().split())

    res = []
    for i in range(len(s)):
        if s[i] in t:
            res.append(s[i])
    
    last = []

    for j in range(len(t)):
        for i in range(j, len(res)):
            if res[i] == t[j]:
                last.append(res[i])

    print(res, last)

