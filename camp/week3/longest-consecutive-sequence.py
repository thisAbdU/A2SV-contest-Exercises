class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) not in numSet:
                currentLength = 0
                while (num + currentLength) in numSet:
                    currentLength += 1
                longest = max(currentLength, longest)
        return longest
                
                
        
        