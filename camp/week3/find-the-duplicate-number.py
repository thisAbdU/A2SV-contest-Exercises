class Solution:
    def findDuplicate(self, nums):
        # Initialize the hare and tortoise pointers
        tortoise = nums[0]
        hare = nums[0]

        # Phase 1: Detect the intersection point of the two pointers
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        # The intersection point is the duplicate number
        return hare

