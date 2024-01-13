class Solution:
    def numberOfSubarrays(self, A, k):
        def atMostK(k):
            result = i = 0

            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1

                result += j - i + 1

            return result

        return atMostK(k) - atMostK(k - 1)
