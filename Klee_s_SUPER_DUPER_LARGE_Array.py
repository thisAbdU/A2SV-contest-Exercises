for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    def min_possible_value(A):
        A.sort()
        n = len(A)

        median = A[(n - 1) // 2]
        return median

# Example Usage:
A = [2, 1, 5, 3, 4]
print(min_possible_value(A))  # Output: 3
