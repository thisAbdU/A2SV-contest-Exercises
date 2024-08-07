def clock_string(arr):
    if arr[0]%12 < arr[2]%12 < arr[1]%12:
        return "YES"
    if arr[0]%12 < arr[3]%12 < arr[1]%12:
        return "YES"
    if arr[0]%12 > arr[2]%12 > arr[1]%12:
        return "YES"
    if arr[0]%12 > arr[3]%12 > arr[1]%12:
        return "YES"
    return "NO"
test = int(input())
for t in range(test):
    arr = list(map(int, input().split()))
    print(clock_string(arr))                                                                