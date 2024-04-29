test = int(input())
for t in range(test):
    N_K = list(map(int, input().split()))
    len_, k = N_K
    nums = list(map(int, input().split()))

    for i in range(k, len_):
        if nums[i-1] < nums[(i - 1)%k]:
            nums[i - 1], nums[(i - 1)%k] = nums[(i - 1)%k], nums[i-1]
    
    for i in range(1, len_):
        nums[i] += nums[i -1]
    
    max_ = -float('inf')
    for j in range(len_):
        if j - k >= 0:
            max_ = max(max_, nums[j] -  nums[j - k])
        else:
            max_ = nums[j]
    print(max_)
    


    



