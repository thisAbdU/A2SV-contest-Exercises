def nene_game(k_q, arr, n):
    res = []
    min_ = min(arr)
    for i in range(k_q[1]):
        res.append(min(min_ -1, n[i]))
    return res


test = int(input())
for t in range(test):
    k_q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    n = list(map(int, input().split()))
    print(*nene_game(k_q, arr, n))
