class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        output = [-1 for i in range(n)]
        stack = deque()

        for i in range(2 * n):

            indx = i % n

            while stack and nums[stack[-1]] < nums[indx]:
                output[stack.pop()] = nums[indx]
            
            if i < n:
                stack.append(indx)

        return output



        