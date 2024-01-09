class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        leftArr = []
        equalArr = []
        rightArr = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                leftArr.append(nums[i])
            elif nums[i] == pivot:
                equalArr.append(nums[i])
            else:
                rightArr.append(nums[i])
        return leftArr + equalArr + rightArr 