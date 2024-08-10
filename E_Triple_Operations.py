MAX = 2*(10**5) + 7

def f(x):
    cnt = 0
    while x:
        x //= 3
        cnt += 1
    return cnt

a = [0] * MAX
prefixsum = [0] * MAX

for i in range(1, MAX-1):
    a[i] = f(i)
    prefixsum[i] = prefixsum[i - 1] + a[i]


for _ in range(int(input())):
    l, r = map(int, input().split())
    print(prefixsum[r] - prefixsum[l - 1] + a[l])
