class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        possitives = []
        negatives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                possitives.append(num)
        
        i = 0
        j = 0
        k = 0
        while k < len(nums):
            if k%2 == 0:
                nums[k] = possitives[i]
                i += 1
                k += 1
            else:
                nums[k] = negatives[j]
                j += 1
                k += 1
        return nums
        