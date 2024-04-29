from collections import defaultdict
import decimal
import math


def max_zero(arr1, arr2):
    max_ = 0
    possible = defaultdict(int)
    for i in range(len(arr1)):
        gd = math.gcd(arr1[i], arr2[i])
        arr1[i] = arr1[i]//gd
        arr2[i] = arr2[i]//gd
    for i in range(len(arr2)):
        if arr1[i] != 0 and arr2[i] != 0:
            poss = decimal.Decimal(-(arr2[i]/arr1[i]))
            possible[poss] += 1
    if possible:
        max_ = max(possible.values())
    print(max_)

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
max_zero(arr1, arr2)