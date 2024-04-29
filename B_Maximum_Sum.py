def maxi_sum(n_k, arr):
    max_sum = -float('inf')
    k = n_k[1]
    modulo = (10 ** 9)
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
    
    while k > 0:
        arr.append(max_sum)
        max_sum = max(arr[-1] + max_sum, max_sum)
        k -= 1
    
    ans = arr[-1] % modulo
    print(ans)

testCase = int(input())
for test in range(testCase):
    n_k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    maxi_sum(n_k, arr)
