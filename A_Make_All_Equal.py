from typing import Counter


for _ in range(int(input())):
    n = int(input()) 
    arr = list(map(int, input().split()))

    count = Counter(arr)

    max_ = 0
    for x in count.values():
        max_ = max(max_, x)

    print(max(0, len(arr) - max_))