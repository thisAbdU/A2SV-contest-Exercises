class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numFrequency = {}
        output = []
        count = 1

        for num in nums:
            if num in numFrequency:
                numFrequency[num] += 1
            else:
                numFrequency[num] = count

        for num in numFrequency:
            if numFrequency[num] > len(nums) / 3:
                output.append(num)

        return output
