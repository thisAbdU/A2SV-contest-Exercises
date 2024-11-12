from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

prefix = 0
cnt = 0
mp = defaultdict(int)
mp[0] = 1 

for num in arr:
    prefix += num
    mod = prefix % n

    if mod < 0:
        mod += n  
        
    cnt += mp[mod]
    mp[mod] += 1

print(cnt)