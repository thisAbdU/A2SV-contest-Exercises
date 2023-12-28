class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        numOcc1 = Counter(nums1)
        numOcc2 = Counter(nums2)
        intersection = set(nums2).intersection(set(nums1))
        for num in intersection:
            count = min(numOcc2[num], numOcc1[num])
            while count > 0:
                output.append(num)
                count -= 1
        return output
        