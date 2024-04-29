import math

def casino(arr):
    count = []
    lcm = math.lcm(*arr)
    for i in range(len(arr)):
        count.append(lcm//arr[i])
    for i in range(len(count)):
        if count[i]%3 != 0 and count[i]%2 != 0 and count[i]//lcm != 1:
            return "Yes"
    return "No"
            
    
n = int(input())
arr = list(map(int, input().split()))
print(casino(arr))

