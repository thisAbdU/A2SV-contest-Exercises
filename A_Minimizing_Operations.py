def minimize_operation(arr):
    maxi = max(arr)
    mini = min(arr)
    return maxi - mini

testCase =int(input())
for test in range(testCase):
    len_ = int(input())
    arr = list(map(int, input().split()))
    print(minimize_operation(arr))
    