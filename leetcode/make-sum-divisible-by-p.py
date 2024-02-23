from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0
        else:
            remainder = total % p
            prefix_sum = 0
            last_seen = {0: -1} 
            min_len = float('inf')

            for i in range(len(nums)):
                prefix_sum = (prefix_sum + nums[i]) % p
                target_remainder = (prefix_sum - remainder + p) % p

                if target_remainder in last_seen:
                    min_len = min(min_len, i - last_seen[target_remainder])

                last_seen[prefix_sum] = i

            return min_len if min_len != float('inf') and min_len != len(nums) else -1

