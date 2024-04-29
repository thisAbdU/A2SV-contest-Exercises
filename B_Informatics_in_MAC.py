from collections import Counter
from typing import List

def find_mex(arr: List[int]) -> int:
    counter = Counter(arr)
    mex = 0
    while mex in counter:
        mex += 1
    return mex

def informatics(n: int, arr: List[int]) -> List[List[int]]:
    mex = find_mex(arr)
    if mex == n:
        return [[-1]]

    divisions = []
    segment_start = 0
    segment_end = -1
    while segment_end < n - 1:
        segment_end += 1
        if arr[segment_end] == mex:
            if segment_start != segment_end:
                divisions.append([segment_start + 1, segment_end])
            segment_start = segment_end + 1

    if segment_start != n:
        divisions.append([segment_start + 1, n])

    if not divisions:
        return [[-1]]
    else:
        return divisions

# Input processing and test case handling
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    result = informatics(n, arr)
    if result == [[-1]]:
        print(-1)
    else:
        print(len(result))
        for segment in result:
            print(segment[0], segment[1])
