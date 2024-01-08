class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, current_sum = 0, 0
        current_len = 0
        min_len = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                current_len = right - left + 1
                min_len = min(current_len, min_len)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
