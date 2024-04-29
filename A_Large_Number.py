def large_number(k, nums):
    insreted = False
    for i in range(len(nums)):
        if k > int(nums[i]):
            nums.insert(i, k)
            insreted = True
            break
    if not insreted:
        nums.append(k)
    nums = [str(n) for n in nums]
    return "".join(nums)
testCase = int(input())
for test in range(testCase):
    n_k = list(map(int, input().split()))
    nums = list(input())
    print(large_number(n_k[1], nums))

