class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def dictIndex(x):
            dictIndx = {num: indx for indx, num in enumerate(arr2)}
            return dictIndx.get(x, float('inf'))

        # Sort arr1 based on the order of elements in arr2
        arr1.sort()
        arr1.sort(key=lambda x: dictIndex(x))
        return arr1