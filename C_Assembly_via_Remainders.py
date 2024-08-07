def assembly(n, arr):
    res = [arr[0] + 1]
    print(arr)
    # for i in range(1, n):
    #     k = arr[i] - (arr[i-1] * (arr[i]//arr[i-1]))
    #     res.append(k)

    return res


tst = int(input())
for t in range(tst):
    n = int(input())
    a = list(map(int, input().split()))
    print(assembly(n, a))
    