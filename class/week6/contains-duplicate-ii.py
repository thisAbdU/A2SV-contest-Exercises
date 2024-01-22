class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        
        for i, num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].append(i)
            else:
                nums_dict[num] = [i]
        
        for num in nums_dict:
            indices = nums_dict[num]
            for i in range(len(indices) - 1):
                if indices[i + 1] - indices[i] <= k:
                    return True
        
        return False
