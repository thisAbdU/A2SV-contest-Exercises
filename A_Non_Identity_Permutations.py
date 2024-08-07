def non_id(n):
    res = [i+1 for i in range(n)]
    res = res[::-1]
    if n%2:
        res[n//2], res[-1] = res[-1], res[n//2]

    print(*res)
    return


test = int(input())
for t in range(test):
    n = int(input())
    non_id(n)