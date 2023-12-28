class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            str_a, str_b = str(a), str(b)
            if str_a + str_b > str_b + str_a:
                return -1
            else:
                return 1
        nums = sorted(nums, key= cmp_to_key(compare))
        return str(int("".join(map(str, nums))))
    