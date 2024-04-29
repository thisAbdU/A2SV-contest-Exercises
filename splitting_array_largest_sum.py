from bisect import bisect_left
from typing import List


def splitArray(nums: List[int], k: int) -> int:
    def is_possible(max_sum):
        no_arr = 0
        sum_ = 0
        for num in nums:
            sum_ += num

            if sum_ > max_sum:
                sum_ = num
                no_arr += 1
                
        return no_arr + 1 <=  k

    left, right = max(nums), sum(nums)

    min_sum = left + bisect_left(range(left, right + 1), True, key=is_possible)

    return min_sum


n_k = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(splitArray(arr, n_k[1]))
