from collections import defaultdict
import heapq


def permutation_string(n, k, arr):
    heapq.heapify(arr)
    while k > 0:
        min_ = heapq.heappop(arr)
        heapq.heappush(arr, min_ + 1)
        k -= 1
    
    min_ = min(arr)
    ans = 1

    for i in arr:
        if i > min_:
            ans += min_
        else:
            ans += min_ - 1

    return ans


test = int(input())
for t in range(test):
    n_k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(permutation_string(n_k[0], n_k[1], arr))
