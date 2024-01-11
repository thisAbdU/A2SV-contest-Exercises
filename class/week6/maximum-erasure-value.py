class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        frequency = {}
        left = 0
        unique_sum = 0
        max_unique_sum = 0

        for right in range(len(nums)):
            unique_sum += nums[right]
            if frequency.__contains__(nums[right]):
                frequency[nums[right]] += 1
            else:
                frequency[nums[right]] = 1

            while frequency[nums[right]] > 1:
                unique_sum -= nums[left]
                frequency[nums[left]] -= 1
                left += 1

            max_unique_sum = max(max_unique_sum, unique_sum)

        return max_unique_sum
