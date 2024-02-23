class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        no_patch = 0
        range_ = 0
        k = 0

        while range_ < n:
            if k < len(nums) and nums[k] <= range_ + 1:
                range_ += nums[k]
                k += 1
            else:
                no_patch += 1
                range_ += (range_ + 1)
        return no_patch
        