class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = -float('inf')
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            if i >= k - 1:
                maxsum = max(currentSum, maxsum)
                currentSum -= nums[i - k + 1]
        return maxsum/k