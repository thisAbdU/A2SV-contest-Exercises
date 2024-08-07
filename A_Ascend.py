def max_increasing(n, arr):
    count = 1
    max_count = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            count += 1
        else:
            count = 1
        max_count = max(count, max_count)
    return max_count

n = int(input())
arr = list(map(int, input().split()))
print(max_increasing(n, arr))

