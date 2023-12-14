class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        nums_index = {index: value for index, value in enumerate(nums)}

        for i in range(len(queries)):
            val, index = queries[i]
            old_value = nums[index]

            nums[index] += val

            if old_value % 2 == 0:
                even_sum -= old_value

            if nums[index] % 2 == 0:
                even_sum += nums[index]

            nums_index[index] = nums[index]
            output.append(even_sum)

        return output
