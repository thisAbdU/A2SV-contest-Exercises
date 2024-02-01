class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        special_sum = 0
        for num in range(n):
            if n%(num+1)== 0:
                special_sum += (nums[num] * nums[num])
        return special_sum