from collections import deque

def distribute_candies(n, m, arr):
    queue = deque()
    for indx, value in enumerate(arr):
        queue.append((indx + 1, value))

    while queue:
        last, last_popped = queue.popleft()
        if last_popped > m:
            last_popped -= m
            queue.append((last, last_popped))
    return last

n_m = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(distribute_candies(n_m[0], n_m[1], arr))