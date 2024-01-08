class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[slow] == val:
                while fast < len(nums) and nums[fast] == val:
                    fast += 1
                if fast < len(nums):
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                else:
                    break
            else:
                slow += 1
                fast += 1
        return slow
