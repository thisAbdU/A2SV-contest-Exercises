def workout(arr):
    c_b_back = [0, 0, 0]

    for i in range(len(arr)):
        c_b_back[i%3] += arr[i]
    
    max_ = c_b_back.index(max(c_b_back))

    if max_ == 0:
        return "chest"
    elif max_ == 1:
        return "biceps"
    else:
        return "back"
    
n = int(input())
arr = list(map(int, input().split()))
print(workout(arr))

