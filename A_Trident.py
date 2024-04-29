def trident(n, arr):
    max_ = max(arr[1:n-1])
    index = arr.index(max_)
    min_left = min_right = float('inf')
    for i in range(index):
        if arr[i] < max_:
            min_left = i
    for j in range(index + 1, n):
        if arr[j] < max_:
            min_right = j
    if min_left != float('inf') and min_right != float('inf'):
        print("YES")
        print(*(min_left + 1, index + 1, min_right + 1))
    else:
        print("NO")
    return 

testCase = int(input())
for i in range(testCase):
    n = int(input())
    arr = list(map(int, input().split()))
    trident(n, arr) 
