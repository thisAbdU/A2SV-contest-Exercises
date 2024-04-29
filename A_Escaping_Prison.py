def escaping_prison(n_h, arr):
    total = 0
    for i in range(n_h[0]):
        total += max(arr[i][0], arr[i][1])
    if total >= n_h[1]:
        print("YES")
    else:
        print("NO")
    return

testCase = int(input())
for test in range(testCase):
    n_h = list(map(int, input().split()))
    arr = []
    for i in range(n_h[0]):
        arra = list(map(int, input().split()))
        arr.append(arra)
    escaping_prison(n_h, arr)