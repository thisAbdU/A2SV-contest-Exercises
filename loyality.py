def loyality(arr, n):
    cnt = 0
    total = 0
    for num in arr:
        total += num
        cnt += 1
        if total >= n:
            return cnt

test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    print(loyality(arr, n))