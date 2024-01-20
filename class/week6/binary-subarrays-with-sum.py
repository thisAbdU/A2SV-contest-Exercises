from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(nums, k):
            left = 0
            no_ofK = 0
            currentSum = 0
            for right in range(len(nums)):
                currentSum += nums[right]
                while currentSum > k:
                    currentSum -= nums[left]
                    left += 1
                no_ofK += right - left + 1
            return no_ofK

        return at_most(nums, goal) - (at_most(nums, goal - 1) if goal > 0 else 0)

