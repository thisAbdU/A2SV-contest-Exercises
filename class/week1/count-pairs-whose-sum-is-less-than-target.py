class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        beg, last = 0, len(nums) - 1
        count = 0
        while beg < last:
            if nums[beg] + nums[last] >= target:
                last -= 1
            else:
                count += last - beg
                beg += 1
                last = len(nums) - 1
        return count