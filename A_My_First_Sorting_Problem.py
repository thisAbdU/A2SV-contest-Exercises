def sort(arr):
    arr.sort()
    print(*arr)

test = int(input())
for t in range(test):
    arr = list(map(int, input().split()))
    sort(arr)