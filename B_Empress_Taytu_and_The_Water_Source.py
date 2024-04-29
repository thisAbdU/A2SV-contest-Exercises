import math


def Impress_taytu(demand, hour, k):
    if sum(hour) > k:
        return -1
    d_h = []
    for i in range(len(demand)):
        d_h.append([demand[i], hour[i]])
    
    left, right = 1, 5 * (10 ** 8)
    while left < right:
        mid = (left + right) // 2
        min_hour = 0
        for i in range(len(d_h)):
            min_hour += (math.ceil(d_h[i][0]/mid) * d_h[i][1])
        if min_hour <= k:
            right = mid
        else:
            left = mid + 1
    return left

testCs = int(input())
for t in range(testCs):
    n_k = list(map(int, input().split()))
    demand = list(map(int, input().split()))
    hour = list(map(int, input().split()))
    print(Impress_taytu(demand, hour, n_k[1]))