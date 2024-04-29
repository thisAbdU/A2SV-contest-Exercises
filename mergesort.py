from typing import List


def merge(left_half,right_half) -> List[int]:
    # write your code here
    output = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            output.append(left_half[i])
            i += 1
        else:
            output.append(right_half[j])
            j += 1
    while i < len(left_half):
        output.append(left_half[i])
        i += 1
    while j < len(right_half):
        output.append(right_half[j])
        j += 1
    return output

def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
   
    return merge(left_half, right_half)

def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
test()
