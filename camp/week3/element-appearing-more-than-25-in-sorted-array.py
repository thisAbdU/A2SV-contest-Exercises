class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        majority = 0.25 * len(arr)
        arr_count = Counter(arr)
        for num in arr_count:
            if arr_count[num] > majority:
                return num
        
        