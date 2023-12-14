class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_dict = {value: index for index, value in enumerate(nums)}
        for i in range(len(operations)):
            if operations[i][0] in index_dict:
                index = index_dict[operations[i][0]]
                nums[index] = operations[i][1]
                index_dict[nums[index]] = index
        return nums