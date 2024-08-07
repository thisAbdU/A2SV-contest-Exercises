import bisect


def contest_proposal(n, a, b):
    a.sort(), b.sort()

    slow = 0
    ans = 0
    for fast in range(n):
        if a[slow] > b[fast]:
            ans += 1
        else:
            slow += 1       

    return ans


test = int(input())
for t in range(test):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    print(contest_proposal(n, arr_a, arr_b))