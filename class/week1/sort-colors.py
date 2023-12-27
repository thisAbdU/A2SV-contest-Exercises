class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxNum = max(nums)
        countNum = [0 for num in range(maxNum + 1)]
        for num in nums:
            countNum[num] += 1
        i, j = 0, 0
        while j < len(countNum):
            if countNum[j] > 0:
                nums[i] = j
                countNum[j] -= 1
                i += 1
            else:
                j += 1
        return nums