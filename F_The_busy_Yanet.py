def the_busy_yanet(arr):
    min_num = min(arr)
    min_index = arr.index(min_num)
    if arr[min_index:] != sorted(arr[min_index:]):
        return -1
    else:
        return min_index
    
testCase = int(input())
for test in range(testCase):
    len_ = int(input())
    arr = list(map(int, input().split()))
    print(the_busy_yanet(arr))