class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        unique_quadruples = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    remaining = target - nums[i] - nums[j] - nums[k]
                    if remaining in seen:
                        quadruple = sorted([nums[i], nums[j], nums[k], remaining])
                        unique_quadruples.add(tuple(quadruple))
            seen.add(nums[i])
            
        return list(unique_quadruples)
