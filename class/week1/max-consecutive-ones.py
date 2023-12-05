class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        right, count, maxCount = 0, 0, 0
        while right < len(nums):
            if nums[right] == 1:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 0
            right += 1
        return maxCount
            
        