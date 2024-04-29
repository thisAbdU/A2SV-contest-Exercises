def make_it_ugly(arr):
    if len(set(arr)) == 1:
        return -1
    slow = 0
    no = 0
    for fast in range(len(arr)):
        if arr[slow] == arr[fast]:
            no += 1
        else:
            break
    return no


test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    print(make_it_ugly(arr))