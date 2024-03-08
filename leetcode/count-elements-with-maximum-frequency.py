class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx_freq = [num for num in freq.values()]
        max_ = max(mx_freq)
        return max_ * mx_freq.count(max_)
        