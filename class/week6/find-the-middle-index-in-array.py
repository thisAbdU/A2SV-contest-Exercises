from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_prefix, right_prefix = [], []
        left_sum, left_pointer, right_sum, right_pointer = 0, 0, 0, len(nums) - 1

        while left_pointer < len(nums):
            left_prefix.append(left_sum)
            left_sum += nums[left_pointer]
            left_pointer += 1

        while right_pointer >= 0:
            right_prefix.append(right_sum)
            right_sum += nums[right_pointer]
            right_pointer -= 1

        right_prefix = right_prefix[::-1]

        for i in range(len(nums)):
            if left_prefix[i] == right_prefix[i]:
                return i

        return -1


