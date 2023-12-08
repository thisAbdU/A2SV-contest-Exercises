
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        result = []
        
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            result.append(nums1[i])
            result.append(nums2[j])
            i += 1
            j += 1

        # Handle the case where one list is longer than the other
        result.extend(nums1[i:])
        result.extend(nums2[j:])

        return result