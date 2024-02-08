class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK_distinct(k):
            start_position = [0 for n in range(len(nums))]
            unique_freq = Counter()
            start = 0
            for end, num in enumerate(nums):
                unique_freq[num] += 1
                while len(unique_freq) > k:
                    unique_freq[nums[start]] -= 1
                    if unique_freq[nums[start]] == 0:
                        unique_freq.pop(nums[start])
                    start += 1
                start_position[end] = start
            return start_position
            
        return abs(sum(a - b for a, b in zip(atMostK_distinct(k), atMostK_distinct(k - 1))))