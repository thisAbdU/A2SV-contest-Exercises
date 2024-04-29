from collections import deque

def expensive_phone(n, arr):
    stack_main = deque()
    count = 0
    for i in range(n):
        while stack_main and arr[i] < stack_main[-1]:
            stack_main.pop()
            count += 1
        else:
            stack_main.append(arr[i])
    return count

testCase = int(input())
for test in range(testCase):
    n = int(input())
    arr = list(map(int, input().split()))
    print(expensive_phone(n, arr))

