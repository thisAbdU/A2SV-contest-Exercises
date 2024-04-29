from collections import Counter
import math


def median_array(n, arr):
    arr.sort()
    mid = math.ceil(len(arr)/2)
    dic = Counter(arr[mid-1:])
    return dic[arr[mid - 1]]

testCase = int(input())
for test in range(testCase):
    n = int(input())
    arr = list(map(int, input().split()))
    print(median_array(n, arr))