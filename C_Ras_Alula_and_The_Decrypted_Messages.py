def ras_alula(n, w):
    prefix = 0
    for i in range(len(w)):
        prefix += (ord(w[i]) - ord('a'))
    prefi = [0]
    current = 0
    for i in range(len(n)):
        current += (ord(n[i]) - ord('a'))
        prefi.append(current)
    j = 0
    while j <= len(n) - len(w):
        if prefi[j + len(w)] - prefi[j] == prefix:
            return "YES"
        j += 1

    return "NO"

test = int(input())
for i in range(test):
    n_h = list(map(int, input().split()))
    n = input()
    w = input()
    print(ras_alula(n, w))
