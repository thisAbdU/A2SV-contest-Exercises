class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0 
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            i += 1

        # Shift zeros to the end
        nums = [num for num in nums if num != 0] + [0] * nums.count(0)
        
        return nums
