def partition(nums, left, right) -> int:
    # Picks a pivot index and returns the index of pivot value in the sorted array
    pivot = nums[0]
    # write your code here
    while left <= right:
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return left 

nums = [10, 0, 2, -5, 3, 2]
print(partition(nums, 0, len(nums) - 1))
nums = sorted(nums)
print(nums)
