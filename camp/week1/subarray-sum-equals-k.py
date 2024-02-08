class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0
        prefix_ = {0:1}
        
        for num in nums:
            current_sum += num
            difference = current_sum - k
            
            count += prefix_.get(difference, 0)
            prefix_[current_sum] = 1 + prefix_.get(current_sum, 0)
        return count