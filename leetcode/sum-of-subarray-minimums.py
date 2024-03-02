class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = deque()
        total = 0
        n = len(arr)
        left = [-1 for i  in range(n)]
        right = [n for i in range(n)]

        for indx, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                stack.pop()
            if stack:
                left[indx] = stack[-1]
            stack.append(indx)

        stack = deque()

        for j in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[j]:
                stack.pop()
            if stack:
                right[j] = stack[-1]
            stack.append(j)
        
        mod = 10**9 + 7

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr))%mod
        return result