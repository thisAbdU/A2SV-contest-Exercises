class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 1
        while fast <len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow, fast = slow + 1, fast + 1
            elif nums[slow] == 0 and nums[fast] == 0:
                fast += 1
            else:
                slow += 1
                fast += 1
        return nums