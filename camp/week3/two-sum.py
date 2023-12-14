class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = sorted((num, index) for index, num in enumerate(nums))
        
        i, j = 0, len(nums) - 1
        
        while i < j:
            current_sum = nums_with_indices[i][0] + nums_with_indices[j][0]
            
            if current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1
            else:
                return [nums_with_indices[i][1], nums_with_indices[j][1]]
        
        return -1
