class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Ascend until peak is reached
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Check if peak is not the first or last element
        if i == 0 or i == n - 1:
            return False

        # Descend from peak
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        # If we reached the end, it's a valid mountain array
        return i == n - 1
