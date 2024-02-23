class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        # distance from left
        sum_of_indices_to_left = {}
        no_of_occurrence_to_left = {}
        sum_index, occur_ = 0, 0
        left_distance = []
        for i, num in enumerate(nums):
            left_distance.append(no_of_occurrence_to_left.get(nums[i], 0) * i - sum_of_indices_to_left.get(nums[i], 0))
            sum_index = sum_of_indices_to_left.get(nums[i], 0)
            sum_index += i
            occur_ = no_of_occurrence_to_left.get(nums[i], 0)
            occur_ += 1
            sum_of_indices_to_left[nums[i]] = sum_index
            no_of_occurrence_to_left[nums[i]] = occur_
        
        # distance from right
        sum_of_indices_to_right = {}
        no_of_occurrence_to_right = {}
        right_distance = []
        for i, num in reversed(list(enumerate(nums))):
            right_distance.append(-no_of_occurrence_to_right.get(nums[i], 0) * i + sum_of_indices_to_right.get(nums[i], 0))
            sum_index = sum_of_indices_to_right.get(nums[i], 0)
            sum_index += i
            occur_ = no_of_occurrence_to_right.get(nums[i], 0)
            occur_ += 1
            sum_of_indices_to_right[nums[i]] = sum_index
            no_of_occurrence_to_right[nums[i]] = occur_
        right_distance.reverse()
        result = [a + b for a, b in zip(left_distance, right_distance)]
        return result


        
        