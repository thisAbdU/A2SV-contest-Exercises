def stair_peak_none(arr):
    if arr[0] < arr[1] < arr[2]:
        return "STAIR"
    elif arr[0] < arr[1] and arr[1] > arr[2]:
        return "PEAK"
    else:
        return "NONE"
    
n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    print(stair_peak_none(arr))