from bisect import bisect_left
from collections import defaultdict

def find_the_car(a, b, q):
    sp = defaultdict(int)
    sp[0] = (a[0]//b[0])
    for i in range(1, len(a)):
        sp[i] = ((a[i] - a[i-1])//(b[i] - b[i - 1]))

    res = []
    for i in q:
        p = bisect_left(a, i)

        if p > 0:
            t = (a[p - 1]//sp[p - 1])
            ans = t + ((i - a[p - 1])//sp[p - 1])
        else:
            ans = i//sp[p]
        res.append(ans)
    return res

test = int(input())
for t in range(test):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    queries = []
    for j in range(q):
        d = int(input())
        queries.append(d)
    print(*find_the_car(a, b, queries))
