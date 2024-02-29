class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k > 1:
            pair_sum = sorted( a + b for a,b in pairwise(weights))
            large_sum = sum(pair_sum[-k+1:])
            small_sum = sum(pair_sum[:k-1])
            print(pair_sum)
            print(large_sum)
            print(small_sum)
            return large_sum - small_sum
        else:
            return 0 