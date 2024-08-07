import math

def maximize(x):
    max_ = 1

    for i in range(x-1, 0, -1):
        max_ = max(max_, math.gcd(x, i))

    return max_


n = int(input())
for t in range(n):
    x = int(input())
    print(maximize(x))

