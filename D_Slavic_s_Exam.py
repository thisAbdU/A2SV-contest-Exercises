def slavic_exam(s, t):
    i = 0
    for j in range(len(s)):
        if i < len(t):
            if s[j] == t[i] or s[j] == '?':
                s[j] = t[i]
                i += 1

    if i == len(t):
        print("YES")
        for i, k in enumerate(s):
                if k == '?':
                    s[i] = s[i-1]
        print("".join(s))
    else:
        print("NO")

for _ in range(int(input())):
    s = input()
    t = input()
    slavic_exam(list(s), list(t))


