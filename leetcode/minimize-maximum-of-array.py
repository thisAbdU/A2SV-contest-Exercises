class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = max_ = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            max_ = max(max_, math.ceil(total/(i+1)))
        return max_


        