import math


def painting_the_ribbon(arr):
    n, m, k = arr
    no_ribbon = math.ceil(n/m)
    if (n - no_ribbon) > k:
        return "YES"
    else:
        return "NO"

test = int(input())
for t in range(test):
    arr = list(map(int, input().split()))
    print(painting_the_ribbon(arr))
