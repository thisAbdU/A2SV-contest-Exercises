class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        len_unique = len(set(nums))
        start, no_complete = 0, 0
        unique_freq = Counter()
        
        for end, num in enumerate(nums):
            unique_freq[num] += 1
            
            while len(unique_freq) == len_unique:
                no_complete += (len(nums) - end)
                unique_freq[nums[start]] -= 1
                if unique_freq[nums[start]] == 0:
                    unique_freq.pop(nums[start])
                start += 1
            
        
        return no_complete