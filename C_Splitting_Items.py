
for _ in range(int(input())):

    n, k = list(map(int, input().split()))
    bobcos = list(map(int, input().split()))

    bobcos.sort(reverse=True)

    for i in range(1, len(bobcos), 2):
        if bobcos[i - 1] - bobcos[i] <= k:
            k -= (bobcos[i - 1] - bobcos[i])
            bobcos[i] = bobcos[i - 1]
        else:
            bobcos[i] += k
            k = 0

    total = 0

    for i in range(1, len(bobcos), 2):
        total += (bobcos[i-1] - bobcos[i])

    if len(bobcos)%2 == 1:
        total += bobcos[-1]
    
    print(total)