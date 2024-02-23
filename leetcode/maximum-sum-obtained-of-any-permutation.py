from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums_index = [0] * len(nums)  
        
        # Increment the starting index of each request
        for start, end in requests:
            nums_index[start] += 1
            if end + 1 < len(nums_index):
                nums_index[end + 1] -= 1

        # Calculate the prefix sum to get the final counts
        current_sum = 0
        for i in range(1, len(nums_index)):
            nums_index[i] += nums_index[i - 1]
        
        nums_index.sort()
        nums.sort()
        
        total = 0
        N = 1e9 + 7
        for i in range(len(nums) - 1, -1, -1):
            total += (nums_index[i] * nums[i]) % N
            total %= N

        
        return int(total)
