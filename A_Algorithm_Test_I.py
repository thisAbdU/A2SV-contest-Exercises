import math


n = int(input())
arr = list(map(int, input().split()))

uniq = len(set(arr))

print(math.perm(uniq))
