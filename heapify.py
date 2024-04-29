def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap_down(arr, n, i)
    return arr

def heap_down(arr, n, current):
    min_ = current
    left_indx = 2 * current + 1
    right_indx = 2 * current + 2

    if left_indx < n and arr[min_] > arr[left_indx]:
        min_ = left_indx
    
    if right_indx < n and arr[min_] > arr[right_indx]:
        min_ = right_indx

    if min_ != current:
        arr[min_], arr[current] = arr[current], arr[min_]
        heap_down(arr, n, min_)

def heap_sort(arr):
    n = len(arr)

    heapify(arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heap_down(arr, i, 0) 

    return arr

arr = [1, 2, 6, 4, 5, 9, 7, 8, 3]
print(heap_sort(arr))