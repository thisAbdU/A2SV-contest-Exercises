class Solution(object):
    def getCommon(self, nums1, nums2):
        st = set(nums1) & set(nums2)
        return min(st) if len(st) else -1