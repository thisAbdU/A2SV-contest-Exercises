class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(nums) - 1:
            output += [nums[i + 1]] * nums[i]
            i += 2
            
        return output