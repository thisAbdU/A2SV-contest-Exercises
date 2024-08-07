from collections import deque


def binary_cut(arr):
    cnt = 1
    stack = deque()
    stack.append(arr[0])
    for i in range(1, len(arr)):
        if stack and stack[-1] <= arr[i]:
            stack.append(arr[i])
        if stack[-1] > arr[i]:
            stack = deque()
            cnt += 1
            stack.append(arr[i])
    return cnt

test = int(input())
for t in range(test):
    a = input()
    arr = list(a)
    print(binary_cut(arr))