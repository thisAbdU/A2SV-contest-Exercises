class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        if length == 1:
            return str(int(n) - 1)
        
        candidates.add(str(10**(length - 1) - 1))


        candidates.add(str(10**length + 1))


        prefix = int(n[:(length + 1) // 2])
        print("prefix", prefix)

        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                candidate = p + p[::-1]
                print("p", p, "p{}", p[::-1])
                print("candidate inside the loop", candidate)
            else:
                candidate = p + p[-2::-1]
            candidates.add(candidate)
            
            print("candidates", candidate)
        
        candidates.discard(n)
        
        closest_palindrome = None
        min_diff = float('inf')
        
        for candidate in candidates:
            diff = abs(int(candidate) - int(n))
            if diff < min_diff or (diff == min_diff and int(candidate) < int(closest_palindrome)):
                min_diff = diff
                closest_palindrome = candidate
        
        return closest_palindrome

solution = Solution()
print(solution.nearestPalindromic(input().strip()))
