n, k = list(map(int, input().split()))
arr = list(input().split())

cnt = 0
for i in arr:
    if i.count('4') + i.count('7') <= k:
        cnt += 1

print(cnt)
